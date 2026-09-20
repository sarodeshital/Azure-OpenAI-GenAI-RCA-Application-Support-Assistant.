# Project Report

## Project

Azure OpenAI GenAI RCA & Application Support Assistant

## Objective

To demonstrate an enterprise-style application support workflow for a GenAI application using Azure OpenAI.

## Problem

GenAI applications can experience authentication, authorization, deployment, throttling, latency, service availability and retrieval-quality problems.

## Solution

The system accepts an incident, classifies the issue, retrieves relevant troubleshooting knowledge and generates a structured RCA using Azure OpenAI.

## Main Workflow

Incident

→ Classification

→ Evidence

→ Retrieval

→ Azure OpenAI

→ RCA

→ Mitigation

→ Validation

→ Prevention

## Technologies

- Python
- FastAPI
- Streamlit
- Azure OpenAI
- RAG
- REST API
- pytest
- Docker
- GitHub Actions

## Sample Incidents

- 401 Authentication
- 403 Authorization
- 404 Resource/Deployment
- 429 Throttling
- 5xx Service Error
- Latency
- RAG Quality

## Limitations

This is a portfolio/simulation project.

It does not represent production client work.

It uses synthetic incident information.

## Future Enhancements

- Azure AI Search
- Application Insights
- Managed Identity
- Azure Key Vault
- Azure Container Apps
- RAG evaluation
- OpenTelemetry
- CI/CD
