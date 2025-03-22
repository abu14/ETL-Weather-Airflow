# **Weather ETL Pipeline with Apache Airflow**

![GitHub contributors](https://img.shields.io/github/contributors/abu14/ETL-Weather-Airflow)
![GitHub forks](https://img.shields.io/github/forks/abu14/ETL-Weather-Airflow?style=social)
![GitHub stars](https://img.shields.io/github/stars/abu14/ETL-Weather-Airflow?style=social)
![GitHub issues](https://img.shields.io/github/issues/abu14/ETL-Weather-Airflow)
![GitHub license](https://img.shields.io/github/license/abu14/ETL-Weather-Airflow)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/abenezer-tesfaye-191579214/)

### **Overview**
The Weather ETL Pipeline is designed to automate the extraction, transformation, and loading (ETL) of weather data using Apache Airflow, Docker, and Astronomer. This project retrieves real-time weather information from the Open Meteo API and stores it in a PostgreSQL database for further analysis.

### 🚀 **Project Structure**
- **dags/**: Contains the Python files for Airflow DAGs.
  - **weather_etl_pipeline.py**: Implements the ETL process by extracting weather data, transforming it, and loading it into the database.
- **Dockerfile**: Specifies the versioned Astro Runtime Docker image for executing the project.
- **requirements.txt**: Lists the Python packages required for the project.
- **plugins/**: Directory for custom or community plugins.
- **airflow_settings.yaml**: Local configuration for Airflow Connections, Variables, and Pools.

### 🛠️ **Requirements**
<p>
<img src="https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/-Apache%20Airflow-017CEE?style=flat&logo=apacheairflow&logoColor=white">
<img src="https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/-Astronomer-00A3E0?style=flat&logo=astronomer&logoColor=white">
<img src="https://img.shields.io/badge/-Open%20Meteo-4B8BBE?style=flat&logo=meteoblue&logoColor=white">
</p>


- **Python**: 3.9+
- **Apache Airflow**: 2.5.0
- **PostgreSQL**: Required for data storage

### 🔧 **Installation Instructions**
1. **Clone the Repository**:
   ```bash
    git clone https://github.com/abu14/ETL-Weather-Airflow.git
    cd ETL-Weather-Airflow
   ```
2. **Build Docker Image**
 ```bash
    docker build -t weather-etl-pipeline .
```

4. **Start Airflow**
  ```bash
    docker-compose up
  ```

### 📌 **Usage**
- Access the Airflow web interface at http://localhost:8080.
- Trigger the weather_etl_pipeline DAG to initiate the ETL process.

### **License**

This project is licensed under the MIT License. See the LICENSE file for details.


