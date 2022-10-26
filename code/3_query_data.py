from query_data_function import search_resources_post

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "<path to your credentials file?"

project_id = "animated-surfer-340819"
location = "us-central1"
dataset_id = "quickstartDataset"
fhir_store_id = "quickstartFHIR"

response = search_resources_post(project_id, location, dataset_id, fhir_store_id)
FHIR_record = response['entry'][0]['resource']

print(FHIR_record)