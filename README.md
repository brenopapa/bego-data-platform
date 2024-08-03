# BEGO Data Platform
Simple, yet cool project.

This repository is used to experiment on how to implement data driven technologies or test new data services providers.

# Chapter One.

Leveraging [Cloud AMQP - RabbitMQ Free Services](https://www.cloudamqp.com/), an ingestion data layer was created, sending [fake](https://faker.readthedocs.io/en/master/) data via Python through RabbitMQ Queue, receiving it by listening to the topic and writing into Parquet files. 

After that, [Duckdb](https://duckdb.org/) is used for data analysis of the Parquet Files.

# Chapter Two (TBD)

Create more queues in RabbitMQ and simulate a live data platform ingestion scenario.

Implement ETL processes using Apache Beam Streaming.

# Chapter Three (TBD)

Use dbt, AirFlow and Streamlit to Process Data, Orquestration and Live Stream data to Dashboards.
