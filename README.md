# MLOps on AWS - End-to-End Machine Learning Pipeline

This repository provides a **fully automated** end-to-end MLOps pipeline that includes **data ingestion, preprocessing, model training, evaluation, deployment, and monitoring** using AWS services. It integrates **CI/CD, infrastructure as code (Terraform), and cloud-based automation (Airflow, Lambda, SageMaker, and CloudWatch).**

## **Project Overview**
This MLOps pipeline is designed to:
- **Automate ML Workflows**: Using Apache Airflow & AWS Step Functions.
- **Ensure Reproducibility**: Track experiments with MLFlow.
- **Version Data & Models**: Store datasets and models using AWS S3 & DVC.
- **Deploy & Serve Models**: API Gateway, AWS Lambda, and SageMaker.
- **Monitor Model Performance**: AWS CloudWatch & drift detection.
- **Infrastructure as Code**: Deploy AWS resources via Terraform.
- **CI/CD for Automation**: Deploy models via GitHub Actions.

## **Architecture Diagram**
```
 ┌───────────────┐    ┌──────────┐    ┌──────────────┐
 │  Data Source  │──▶│  S3 Raw  │──▶│ AWS Glue/ETL │
 └───────────────┘    └──────────┘    └──────────────┘
       │                               │
       ▼                               ▼
 ┌──────────────┐    ┌────────────┐    ┌──────────────┐
 │ Feature Store│──▶│  MLFlow   │──▶│ SageMaker Train │
 └──────────────┘    └────────────┘    └──────────────┘
       │                               │
       ▼                               ▼
 ┌────────────┐    ┌───────────────┐    ┌──────────────┐
 │  Model Repo│──▶│  AWS Lambda  │──▶│ API Gateway   │
 └────────────┘    └───────────────┘    └──────────────┘
       │                               │
       ▼                               ▼
 ┌──────────────┐    ┌──────────────┐
 │  CloudWatch  │──▶│ Model Monitor │
 └──────────────┘    └──────────────┘
```

---

## **Setup & Installation**

```sh
pip install -r requirements.txt
```
#### **Set Up Conda Environment**
```sh
conda env create -f conda.yaml
conda activate mlops-env
```
#### **Configure AWS Credentials**
```sh
aws configure
```

---
## **Running the MLOps Pipeline**

### **Step 1: Data Ingestion**
Fetch and store raw data in **AWS S3**
```sh
python src/data/ingest_data.py
```

### **Step 2: Feature Engineering**
Preprocess data and store transformed data in **S3**
```sh
python src/features/feature_engineering.py
```

### **Step 3: Model Training**
Train and store model with **MLFlow tracking**
```sh
python src/models/train_model.py
```

### **Step 4: Deploy Model on AWS Lambda**
Deploy trained model as an API endpoint
```sh
python src/deployment/deploy_lambda.py
```

### **Step 5: Test API Deployment**
```sh
curl -X POST "https:/tej-api/predict" -d '{"data": [5, 116, 74, 0, 0, 25.6, 0.201, 30]}'
```

---
## **Infrastructure Deployment using Terraform**

### **Step 1: Initialize Terraform**
```sh
cd terraform
terraform init
```

### **Step 2: Deploy AWS Resources**
```sh
terraform apply -auto-approve
```

### **Step 3: Destroy AWS Resources**
```sh
terraform destroy -auto-approve
```

---
## **Pipeline Orchestration using Apache Airflow**

### **Start Airflow Scheduler & Webserver**
```sh
airflow scheduler & airflow webserver
```

### **Trigger DAG Manually**
```sh
airflow dags trigger ml_pipeline
```

---
## **CI/CD - GitHub Actions Workflow**

A GitHub Actions pipeline (`.github/workflows/ci-cd-pipeline.yml`) is included to:
- Run tests
- Deploy the trained model to AWS Lambda
- Monitor deployments

### **Trigger Deployment**
Push changes to the `main` branch:
```sh
git add .
git commit -m "Updated Model"
git push origin main
```

This will automatically trigger the **GitHub Actions** pipeline to deploy the model.

---
## **Monitoring & Logging**
### **View Lambda Logs using AWS CloudWatch**
```sh
aws logs tail /aws/lambda/MLPredictor --follow
```

### **Monitor Model Performance**
Run model monitoring script:
```sh
python src/monitoring/monitor_model.py
```

---
