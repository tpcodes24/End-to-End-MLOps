# MLOps on AWS - End-to-End Machine Learning Pipeline

This repository provides a **fully automated** MLOps pipeline for data ingestion, preprocessing, model training, evaluation, deployment, and monitoring using AWS services.

## Features
- **Data Ingestion & Versioning**: AWS S3 + DVC
- **Feature Engineering**: Scikit-learn transformations
- **Model Training & Tracking**: Amazon SageMaker + MLFlow
- **Deployment**: AWS Lambda + API Gateway
- **Monitoring**: AWS CloudWatch & Model Drift Detection
- **Pipeline Automation**: Apache Airflow + Terraform for AWS infra
- **CI/CD**: GitHub Actions for auto-deploy

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Set up AWS credentials: `aws configure`
3. Run pipeline: `airflow dags trigger ml_pipeline`
4. Deploy API: `python src/deployment/deploy_lambda.py`
