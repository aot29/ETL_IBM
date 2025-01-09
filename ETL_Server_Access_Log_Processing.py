from datetime import timedelta
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import requests

input_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt'
extracted_file = 'extracted-data.txt'
transformed_file = 'transformed.txt'
output_file = 'data_for_analytics.csv'

def extract():
  global input_file, extracted_file
  print("Extract")
  # download the file
  
  # read file
  with open(extracted_file, 'w') as outfile:
    content = requests.get(input_url, stream=True).content
    for line in content:
      fields = line.split('#')
      if len(fiels) >= 6:
        outfile.write(f"{fields[0]}:{fields[3]}\n")

def transform():
  global extracted_file, transformed_file
  print("Transform")
  with open(extracted_file, 'r') as infile, open(transformed_file, 'w') as outfile:
    for line in infile:
      processed_line = line.replace(':', ',')
      outfile.write(processed_line + '\n')

def load():
  global transformed_file, output_file
  print("Load")
  with open(transformed_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
      outfile.wrie(line + '\n')

def check():
  global output_file
  print("Check")
  with open(output_file, 'r') as infile:
    for line in infile:
      print(line)

default_args = {
  'owner': 'aot29',
  'start_date': days_ago(0),
  'email': ['bla@example.com'],
  'retries': 0,
  'retry_delay': timedelta(minutes=5)
}

# DAG definition
dag = DAG(
  'ETL_Server_Access_Log_Processing',
  default_args=default_args,
  description='Example server access logs processing',
  schedule_interval=timedelta(days=1)
)

# Tasks definitions
execute_extract = PythonOperator(
  task_id='extract',
  python_callable=extract,
  dag=dag
)

execute_transform = PythonOperator(
  task_id='transform',
  python_callable=transform,
  dag=dag
)

execute_load = PythonOperator(
  task_id='load',
  python_callable=load,
  dag=dag
)

execute_check = PythonOperator(
  task_id='check',
  python_callable=check,
  dag=dag
)

# Task pipeline
execute_extract >> execute_transform >> execute_load >> execute_check
