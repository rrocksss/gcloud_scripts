from google.cloud import bigquery

client =  bigquery.Client(project="richard-59498")

# Perform a query.
QUERY = (
    'SELECT date_column_1 as date FROM `richard-59498.experiment.example_table_1` LIMIT 1')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish
for row in rows:
    print(row.date)