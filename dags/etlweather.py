from airflow import DAG
from airflow.providers.https.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago


# Latitude and Longiture
LATITUDE = '51.5074'
LONGITUDE = '-0.1278'

POST_GRESQL_CONN_ID = 'postgres_default'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

#DAG 
with DAG(dag_id='weather_etl_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         #tags=['example'],
         catchup=False) as dag:

    @task()
    def extract_weather_data():
        """Extract weahter data from an API using Airflow HttpHook"""
        
        # Get the API connection using the httphook
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')
        
        ## Build the API endpoint
        ## https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current_weather=true
        endpoint=f'/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true'         
        
        #request via the http hook
        response = http_hook.run(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'API request failed: {response.status_code}')


    @task()
    def transform_weather_data(weather_data):
        """Transform the weather data"""
        # Extract the relevant data from the response
        current_weather = weather_data['current_weather']
        
        # Return transformated data
        transformed_data = {
            'latitude': LATITUDE,
            'longitude': LONGITUDE,
            'temperature': current_weather['temperature'],
            'windspeed': current_weather['windspeed'],
            'winddirection': current_weather['winddirection'], 
            'weathercode': current_weather['weathercode']
        }
        return transformed_data
  
    @task()
    def load_weather_data(weather_data):
        """"Load the new transformed weaether data to the Postgres database"""
        # Get the Postgres connection
        pg_hook = PostgresHook(postgres_conn_id=POST_GRESQL_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        # save and creaate a table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                latitude VARCHAR(50),
                longitude VARCHAR(50),
                temperature FLOAT,
                windspeed FLOAT,
                winddirection FLOAT,
                weathercode INTEGER,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cursor.close()

    ## DAG worflow - pipeline
    wather_data = extract_weather_data()
    transform_weather_data = transform_weather_data(wather_data)
    load_weather_data(transform_weather_data)