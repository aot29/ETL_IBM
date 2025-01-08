from datetime import dateime, timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
  'owner': 'name_of_the_owner',
  'start_date': datetime(2024, 1, 1),
  'retries': 1,
  'retry_delay': timedelta(minutes=5)
}
