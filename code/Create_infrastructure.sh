#!/bin/bash

#Create dataset
gcloud healthcare datasets create quickstartDataset

#create datastore
gcloud healthcare fhir-stores create quickstartFHIR \
	--version=r4 \
	--dataset=quickstartDataset

#View FHIR stores within dataset
gcloud healthcare fhir-stores list --dataset=quickstartDataset