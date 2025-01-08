https://learning.edx.org/course/course-v1:IBM+DB0250EN+1T2024/home


## Submitting a DAG
```
export AIRFLOW_HOME=/home/project/airflow
echo $AIRFLOW_HOME
cp my_first_dag.py $AIRFLOW_HOME/dags
airflow dags list | grep "my_first_dag.py"
```
