# Google Cloud Healthcare API Quickstart
The following tutorial is a brief overview of how to setup and use Google's Cloud Healthcare API. To learn more, visit our **[documentation](https://cloud.google.com/healthcare-api)**

### 0. Install Dependencies
Please **[install](https://cloud.google.com/sdk/docs/install)** and **[initialize](https://cloud.google.com/sdk/docs/initializing)** the gcloud CLI. We will use the CLI to create, manage, and destroy our healthcare datasets.

### 1. Setup Healthcare API
The code in the following section can be found in the create_infrastructure.sh script. Feel free to execute the entire script, or follow along section by section.


The first step to using the Cloud Healthcare API is to setup a dataset, which acts as a centralized location for your healthcare data. The dataset can be configured as follows:
```
gcloud healthcare datasets create quickstartDataset
```

With the dataset created, we can now create one or more datastores within this dataset, designed to hold all different types of medical data, such as FHIR, DICOM and HIL7v2. To learn more about what types of data can be stored, view our **[data model](https://cloud.google.com/healthcare-api/docs/concepts/introduction#data_model)**

In this case, we will be creating a sample FHIR store, as shown below:
```
gcloud healthcare fhir-stores create quickstartFHIR \
	--version=r4 \
	--dataset=quickstartDataset
```
