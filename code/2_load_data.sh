#!/bin/bash

#Copy Data to GCS bucket
gsutil cp data/resources.ndjson gs://<your GCS bucket>

#Import Data
gcloud healthcare fhir-stores import gcs quickstartFHIR \
	--gcs-uri=gs://<your GCS bucket> \
	--dataset=quickstartDataset \
	--content-structure=RESOURCE