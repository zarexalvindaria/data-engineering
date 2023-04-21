#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# Set defaults if no arguments are passed from CLI.
pushd "$(dirname "$0")/.."

export SLUGIFY_USES_TEXT_UNIDECODE=yes
# Create a virtual environment, as the Airflow process we're trying to install conflicts with the DataCamp Docker image.
pipenv install \
  --dev \
  --skip-lock  # speed up the installation process, merely for the DataCamp exercises
# Switch to unit-test mode
export AIRFLOW__CORE__UNIT_TEST_MODE=True
export AIRFLOW__CORE__LOGGING_LEVEL=ERROR
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW_HOME=$(pwd)

# Airflow will log an error message that a DAG could not be loaded. That's
# because it depends on a Variable that can only get loaded once the db has
# been initialized. That's an expected race condition. Workaround would be to
# move the dag folder temporarily before initializing. It's only a logged error,
# so won't hurt the tests.
pipenv run airflow initdb

# Import variables into the local Airflow
. script/configure

pipenv run airflow variables --set environment dev



# Add the correct paths to discover the DAGs and plugins
export AIRFLOW__CORE__DAGS_FOLDER=dags
export AIRFLOW__CORE__PLUGINS_FOLDER=plugins

# Run tests.
pipenv run pytest .
