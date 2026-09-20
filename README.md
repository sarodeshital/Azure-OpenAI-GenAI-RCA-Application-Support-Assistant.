# Azure OpenAI GenAI RCA & Application Support Assistant

An interview-ready portfolio project demonstrating an enterprise-style application support workflow using Azure OpenAI, Python, RAG, FastAPI, Streamlit and structured Root Cause Analysis (RCA).

## Project Objective

The objective of this project is to simulate how an Application Support Engineer can investigate and troubleshoot issues in an Azure OpenAI-powered GenAI application.

The workflow is:

Incident
→ Error Classification
→ Evidence Collection
→ Knowledge Retrieval
→ Azure OpenAI
→ RCA
→ Resolution Recommendation
→ Validation
→ Preventive Action

## Business Problem

Enterprise GenAI applications can experience:

- Authentication failures
- Authorization failures
- Incorrect deployments
- API errors
- Throttling
- High latency
- Service availability problems
- Poor RAG retrieval
- Incorrect or hallucinated answers

Support engineers need a structured process to identify the failing component, investigate evidence, determine probable root cause and document resolution.

This project provides decision-support for that workflow.

## Key Features

- Azure OpenAI integration
- Python backend
- FastAPI REST API
- Streamlit support dashboard
- RAG-based troubleshooting knowledge retrieval
- Incident classification
- 401 troubleshooting
- 403 troubleshooting
- 404 troubleshooting
- 429 troubleshooting
- 5xx troubleshooting
- Latency investigation
- RAG quality troubleshooting
- Structured RCA generation
- Evidence-based recommendations
- Unit testing
- GitHub Actions CI
- Secure environment configuration
- Docker support

## Architecture

```text
                    +----------------------+
                    |      Support User    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Streamlit UI       |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   FastAPI Backend    |
                    +----------+-----------+
                               |
              +----------------+----------------+
              |                                 |
              v                                 v
     +------------------+              +------------------+
     | Incident Analyzer|              | RAG Retrieval    |
     +---------+--------+              +--------+---------+
               |                                |
               |                                v
               |                       Knowledge Base
               |                                |
               +----------------+---------------+
                                |
                                v
                       +----------------+
                       | Azure OpenAI   |
                       +--------+-------+
                                |
                                v
                       +----------------+
                       | Structured RCA |
                       +--------+-------+
                                |
                                v
                       +----------------+
                       | Validation &   |
                       | Prevention     |
                       +----------------+
