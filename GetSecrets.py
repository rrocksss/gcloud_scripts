from google.cloud import secretmanager

def access_secret_version(project_id, secret_id, version_id="latest"):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Get the secret payload and decode it.
    secret_value = response.payload.data.decode("UTF-8")
    return secret_value

# Example usage
project_id = "richard-59498"
secret_id = "some-credential"
secret_value = access_secret_version(project_id, secret_id)
print(f"Secret Value: {secret_value}")