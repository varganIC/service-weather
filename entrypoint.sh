#!/bin/bash
set -e

echo "--------------- Applying DB migrations..."
airflow db migrate

echo "---------------- Creating admin user..."
airflow users create \
  --username "${AIRFLOW_ADMIN_USERNAME}" \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email "${AIRFLOW_ADMIN_EMAIL}" \
  --password "${AIRFLOW_ADMIN_PASSWORD}"

echo "--------------- Starting scheduler..."
airflow scheduler &

echo "--------------- Starting webserver..."
exec airflow webserver
