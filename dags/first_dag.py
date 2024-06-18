
from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'gret',
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'first_dag',
    default_args=default_args,
    description='A simple email DAG',
    schedule_interval='0 4 * * *',
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

send_email = EmailOperator(
    task_id='send_email',
    to='susmapant@gmail.com',
    subject='Daily Greetings',
    html_content='Good Morning Didi. Hope you have a wonderful day.',
    dag=dag,
)

start >> send_email
