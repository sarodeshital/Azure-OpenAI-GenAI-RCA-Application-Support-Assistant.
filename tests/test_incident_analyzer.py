from app.incident_analyzer import (
    classify_error,
    build_evidence
)

from app.models import IncidentRequest


def test_429_classification():

    classification, action = classify_error(
        "429"
    )

    assert classification == "Throttling"

    assert "request rate" in action.lower()


def test_401_classification():

    classification, _ = classify_error(
        "401"
    )

    assert classification == "Authentication"


def test_evidence_contains_error():

    incident = IncidentRequest(

        incident_id="INC-1",

        service="test",

        error_code="429",

        description="test",

        logs=["429"]
    )

    evidence = build_evidence(
        incident
    )

    assert any(
        "429" in item
        for item in evidence
    )
