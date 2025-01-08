from datetime import dateime, timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

# default arguments
default_args = {
  'owner': 'name_of_the_owner',
  'start_date': datetime(2024, 1, 1),
  'retries': 1,
  'retry_delay': timedelta(minutes=5)
}

# dag definition
dag = DAG(
  'simple_example',
  description='Simple example DAG',
  default_args=default_args,
  schedule=timedelta(seconds=5)
)

# task definitions
task1 = BashOperator(
  task_id='print_date',
  bash_command='echo \'Greetings, the date and time are \'',
  dag=dag
)
task2 = BashOperator(
 task_id='print_date',
 bash_command='date',
 dag=dag
)

# task pipeline
task1 >> task2
