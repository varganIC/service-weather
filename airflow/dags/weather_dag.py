from datetime import datetime

from airflow.operators.python import PythonOperator
from weather.weather_utils import check_latest, fetch_and_store

from airflow import DAG

with DAG(
    dag_id="daily_weather_collector",
    schedule_interval="@daily",
    start_date=datetime.utcnow(),
    catchup=False,
    tags=["weather"],
    description="Сбор погоды для городов"
) as dag:
    fetch_task = PythonOperator(
        task_id="fetch_weather",
        python_callable=fetch_and_store
    )

    check_task = PythonOperator(
        task_id="check_weather_upload",
        python_callable=check_latest
    )

    fetch_task >> check_task
