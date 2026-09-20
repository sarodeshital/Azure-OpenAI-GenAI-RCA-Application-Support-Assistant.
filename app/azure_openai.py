from openai import AzureOpenAI

from .config import settings


def get_client():

    if not all(
        [
            settings.azure_openai_endpoint,
            settings.azure_openai_api_key,
            settings.azure_openai_chat_deployment
        ]
    ):

        raise RuntimeError(
            "Azure OpenAI configuration is incomplete. "
            "Please configure the required values in .env."
        )

    return AzureOpenAI(
        api_key=settings.azure_openai_api_key,
        api_version=settings.azure_openai_api_version,
        azure_endpoint=settings.azure_openai_endpoint
    )


def generate_rca(
    incident,
    classification,
    evidence,
    retrieved_docs
):

    client = get_client()

    knowledge_context = "\n\n".join(
        [
            f"DOCUMENT: {doc['name']}\n{doc['content']}"
            for doc in retrieved_docs
        ]
    )

    logs = "\n".join(incident.logs)

    prompt = f"""
You are an enterprise application-support RCA assistant.

Do not invent evidence.

Clearly distinguish observed evidence from hypotheses.

Provide decision support only.

Do not claim autonomous production remediation.

Incident ID:
{incident.incident_id}

Service:
{incident.service}

Error:
{incident.error_code}

Description:
{incident.description}

Logs:
{logs}

Classification:
{classification}

Observed Evidence:
{chr(10).join(evidence)}

Troubleshooting Knowledge:
{knowledge_context}

Return the following sections:

Probable Root Cause

Evidence

Immediate Actions

Validation Steps

Preventive Actions
"""

    response = client.chat.completions.create(

        model=settings.azure_openai_chat_deployment,

        messages=[
            {
                "role": "system",
                "content":
                "You are a careful enterprise application support assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.1
    )

    return response.choices[0].message.content
