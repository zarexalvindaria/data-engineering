# Define the ETL function
def etl():
    film_df = ____()
    film_df = ____(____)
    ____(____)

# Define the ETL task using PythonOperator
etl_task = PythonOperator(task_id='etl_film',
                          python_callable=____,
                          dag=dag)

# Set the upstream to wait_for_table and sample run etl()
etl_task.____(wait_for_table)
etl()

-----

# Define the ETL function
def etl():
    film_df = extract_film_to_pandas()
    film_df = transform_rental_rate(film_df)
    load_dataframe_to_film(film_df)

# Define the ETL task using PythonOperator
etl_task = PythonOperator(task_id='etl_film',
                          python_callable=etl,
                          dag=dag)

# Set the upstream to wait_for_table and sample run etl()
etl_task.set_upstream(wait_for_table)
etl()