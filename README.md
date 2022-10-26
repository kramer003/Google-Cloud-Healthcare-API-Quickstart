# Google Cloud Healthcare API Quickstart
The following tutorial is a brief overview of how to setup and use Google's Cloud Healthcare API. To learn more, visit our **[documentation](https://cloud.google.com/healthcare-api)**.

In this tutorial, you will learn how to:
1. Setup the Cloud Healthcare API
2. Load data into a FHIR store
3. Retrieve (query) data from a FHIR store
4. De-identify and purge customer PII

### 0. Install Dependencies
Please **[install](https://cloud.google.com/sdk/docs/install)** and **[initialize](https://cloud.google.com/sdk/docs/initializing)** the gcloud CLI. We will use the CLI to create, manage, and destroy our healthcare datasets.

### 1. Setup the Cloud Healthcare API
The code in the following section can be found in the **[code/create_infrastructure.sh](https://github.com/kramer003/Google-Cloud-Healthcare-API-Quickstart/blob/main/code/1_create_infrastructure.sh)** script. Feel free to execute the entire script, or follow along section by section.


The first step to using the Cloud Healthcare API is to setup a dataset, which acts as a centralized location for your healthcare data. The dataset can be configured as follows:
```
gcloud healthcare datasets create quickstartDataset
```

With the dataset created, we can now create one or more datastores within this dataset, designed to hold all different types of medical data, such as FHIR, DICOM and HIL7v2. To learn more about what types of data can be stored, view our **[data model](https://cloud.google.com/healthcare-api/docs/concepts/introduction#data_model)**.

In this case, we will be creating a sample FHIR store, as shown below:
```
gcloud healthcare fhir-stores create quickstartFHIR \
	--version=r4 \
	--dataset=quickstartDataset
```

As a last step, let's ensure our FHIR store was setup correctly with the `list` command
```
gcloud healthcare fhir-stores list --dataset=quickstartDataset
```
![data](images/FHIR_Store.png)

### 2. Load data into a FHIR store
The **[data/resources.ndjson](https://github.com/kramer003/Google-Cloud-Healthcare-API-Quickstart/blob/main/data/resources.ndjson)** file contains information on 10 sample patients following the **[Resource](https://console.cloud.google.com/healthcare/browser/locations/us-central1/datasets/quickstartDataset/fhirStores/quickstartFHIR/import?project=animated-surfer-340819)** content structure.

All patients are structured in the following json format:
```
{"birthDate":"1970-01-01","gender":"female","id":"2938bb9e-1f16-429e-8d44-9508ab0e4151","name":[{"family":"Smith","given":["Darcy"],"use":"official"}],"resourceType":"Patient"}
```

I typically recommend working with small dummy data while you get the hand of the Healthcare API. As you become more comfortable, I'd recommend using **[Synthea](https://synthea.mitre.org/)** to generate synthetic healthcare data that more closely mimics your final production state.

The code in the following section can be found in the **[code/2_load_data.sh](https://github.com/kramer003/Google-Cloud-Healthcare-API-Quickstart/blob/main/code/2_load_data.sh)** file. 

As a prerequisite of loading our data into our FHIR store, we must first move the data to Cloud Storage, as follows:
```
gsutil cp data/resources.ndjson gs://<your GCS bucket>
```

With the data in Cloud Storage, we can now import into our FHIR store:
```
gcloud healthcare fhir-stores import gcs quickstartFHIR \
	--gcs-uri=gs://<your GCS bucket> \
	--dataset=quickstartDataset \
	--content-structure=RESOURCE
```

If your import was successful, you should see a `complete...done` message in the log. A good way to double check. As a quick sanity check, it is a good idea to check your Patients in the FHIR viewer, and ensure they are correctly loaded.

![data](images/FHIR_viewer.png)

### 3. Retrieve data from a FHIR store