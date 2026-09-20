import logging

from fastapi import FastAPI, HTTPException

from .models import IncidentRequest
from .incident_analyzer import (
    classify_error,
    build_evidence
)
from .rag import retrieve
from .azure_openai import generate_rca
from .rca_engine import parse_model_output
from .config import settings


logging.basicConfig(
    level=settings.log_level
)

logger = logging.getLogger(
    settings.app_name
)


app = FastAPI(

    title=(
        "Azure OpenAI GenAI RCA "
        "& Application Support Assistant"
    ),

    version="1.0.0"
)


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": settings.app_name
    }


@app.post("/analyze")
def analyze(
    incident: IncidentRequest
):

    try:

        classification, baseline_action = (
            classify_error(
                incident.error_code
            )
        )

        evidence = build_evidence(
            incident
        )

        documents = retrieve(

            f"{incident.error_code} "
            f"{incident.service} "
            f"{incident.description}"
        )

        model_output = generate_rca(

            incident,

            classification,

            evidence,

            documents
        )

        parsed_output = parse_model_output(
            model_output
        )

        return {

            "incident_id":
                incident.incident_id,

            "classification":
                classification,

            "baseline_action":
                baseline_action,

            "evidence":
                evidence,

            "retrieved_knowledge":
                [
                    document["name"]
                    for document in documents
                ],

            "model_rca":
                parsed_output,

            "raw_model_output":
                model_output
        }

    except Exception as error:

        logger.exception(
            "Incident analysis failed"
        )

        raise HTTPException(

            status_code=500,

            detail=str(error)
        )
