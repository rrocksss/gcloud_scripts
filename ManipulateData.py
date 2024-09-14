from google.cloud import bigquery

client = bigquery.Client(project="richard-59498")

table_id = "richard-59498.experiment.example_table_1"

# Create new records to insert
rows_to_insert = [
    {"date_column_1": "2024-09-10T12:30:00.123456"}
]

# Insert the rows into the table
errors = client.insert_rows_json(table_id, rows_to_insert)

# Check if there were any errors during insertion
if errors == []:
    print("A new row has been added successfully.")
else:
    print(f"Errors occurred: {errors}")