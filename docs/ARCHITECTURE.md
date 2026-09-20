# Architecture

## Current Portfolio Architecture

```text
Streamlit
    |
    v
FastAPI
    |
    +---- Incident Analyzer
    |
    +---- Knowledge Retrieval
    |
    +---- Azure OpenAI
    |
    +---- RCA Parser


## Production-Oriented Architecture

User
 |
 v
Application Gateway
 |
 v
Azure Container Apps / AKS
 |
 v
FastAPI
 |
 +------ Azure OpenAI
 |
 +------ Azure AI Search
 |
 +------ Application Insights
 |
 +------ Key Vault
 |
 +------ Microsoft Entra ID
