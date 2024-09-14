from google.cloud import bigquery

client =  bigquery.Client(project="richard-59498")

#list all datasets in the project
# datasets = list(client.list_datasets())

dataset =  client.get_dataset("richard-59498.experiment")
#can also use bigquery.Dataset(dataset id) but it is usually used for defining or creating a dataset in BigQuery

# Check if there are any datasets
# if datasets:
#     print("Datasets in project 'richard-59498':")
#     for dataset in datasets:
#         print(dataset.dataset_id)
# else:
#     print("No datasets found.")

print(f"Dataset Location: {dataset.location}")
print(f"Dataset Labels: {dataset.labels}")
print(f"Dataset Description: {dataset.description}")
print(f"Dataset Expiration: {dataset.default_table_expiration_ms}")