#!/bin/bash

#Download Synthea data
wget https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_fhir_r4_sep2019.zip

#Unzip the data
unzip synthea_sample_data_fhir_r4_sep2019.zip

#Copy Data to GCS bucket
gsutil -m cp -r fhir gs://<your GCS bucket>

#Import Data
gcloud healthcare fhir-stores import gcs quickstartFHIR \
	--gcs-uri=gs://<your GCS bucket>/fhir/* \
	--dataset=quickstartDataset \
	--content-structure=bundle-pretty