# Create a DAG object
dag = ____(
  dag_id='optimize_diaper_purchases',
  default_args={
    # Don't email on failure
    'email_on_failure': ____,
    # Specify when tasks should have started earliest
    '____': ____(2019, 6, 25)
  },
  # Run the DAG daily
  schedule_interval='____')

# -------------- #

# Create a DAG object
dag = DAG(
  dag_id='optimize_diaper_purchases',
  default_args={
    # Don't email on failure
    'email_on_failure': False,
    # Specify when tasks should have started earliest
    'start_date': datetime(2019, 6, 25)
  },
  # Run the DAG daily
  schedule_interval='@daily')