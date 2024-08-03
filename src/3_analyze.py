import duckdb
duckdb.sql("SELECT COUNT(DISTINCT id) DISTINCT_CLIENTS FROM 'data/bronze/customers/*.parquet';").show()

duckdb.sql("SELECT COUNT(DISTINCT name) DISTINCT_CLIENTS_2024 FROM 'data/bronze/customers/*.parquet' WHERE date_of_birth >= '2024-01-01';").show()