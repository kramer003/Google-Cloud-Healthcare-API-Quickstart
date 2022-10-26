#https://cloud.google.com/healthcare-api/docs/how-tos/fhir-search

def search_resources_post(project_id, location, dataset_id, fhir_store_id):
    """
    Searches for resources in the given FHIR store. Uses the
    _search POST method and a query string containing the
    information to search for. In this sample, the search criteria is
    'family:exact=Smith' on a Patient resource.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
    before running the sample."""
    # Imports Python's built-in "os" module
    import json
  
    # Imports the google.auth.transport.requests transport
    from google.auth.transport import requests

    # Imports a module to allow authentication using a service account
    from google.oauth2 import service_account

    # Gets credentials from the environment.
    credentials = service_account.Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    )
    scoped_credentials = credentials.with_scopes(
        ["https://www.googleapis.com/auth/cloud-platform"]
    )
    # Creates a requests Session object with the credentials.
    session = requests.AuthorizedSession(scoped_credentials)

    # URL to the Cloud Healthcare API endpoint and version
    base_url = "https://healthcare.googleapis.com/v1"

    # TODO(developer): Uncomment these lines and replace with your values.
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, location)

    fhir_store_path = "{}/datasets/{}/fhirStores/{}/fhir".format(
        url, dataset_id, fhir_store_id
    )

    resource_path = "{}/Patient/_search?family:exact=William".format(fhir_store_path)

    # Sets required application/fhir+json header on the request
    headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
    
    response = session.post(resource_path, headers=headers)
    response.raise_for_status()
    
    resources = response.json()

    return resources