#!/bin/bash

#create FHIR store to store de-identified data
gcloud healthcare fhir-stores create quickstartFHIR-deIdentified \
	--version=r4 \
	--dataset=quickstartDataset

#Deidentify quiststartFHIR and export it to new FHIR store
gcloud healthcare fhir-stores deidentify quickstartFHIR \
	--dataset=quickstartDataset \
	--destination-store=projects/animated-surfer-340819/locations/us-central1/datasets/quickstartDataset/fhirStores/quickstartFHIR-deIdentified