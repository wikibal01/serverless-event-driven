# Serverless Event-Driven Microservices with Automated Monitoring and Scaling

## Introduction

This project demonstrates an event-driven microservices architecture using AWS Lambda. The microservices are automatically monitored and scaled based on workload.

## Architecture

The system includes:
- **AWS Lambda**: For running the microservices.
- **AWS API Gateway**: To expose the Lambda functions as REST APIs.
- **AWS DynamoDB**: For data storage.
- **AWS CloudWatch**: For monitoring, logging, and triggering alarms.
- **Terraform**: For Infrastructure as Code (IaC).
- **Serverless Framework**: To simplify the deployment of serverless resources.
- **GitHub Actions**: For CI/CD automation.

## Setup Instructions

### Prerequisites

- AWS account
- Terraform installed
- Serverless Framework installed
- GitHub Actions setup with AWS credentials

### Deploying with Terraform

1. Initialize Terraform:
    ```bash
    terraform init
    ```

2. Apply the Terraform configuration:
    ```bash
    terraform apply
    ```

### Deploying with Serverless Framework

1. Install dependencies:
    ```bash
    npm install
    ```

2. Deploy the service:
    ```bash
    serverless deploy
    ```

## Usage

- API endpoints are exposed via API Gateway.
- Lambda functions are triggered based on events like HTTP requests or scheduled events.

## Monitoring and Scaling

- CloudWatch automatically monitors the performance of the Lambda functions.
- CloudWatch alarms trigger notifications and auto-scaling events.
