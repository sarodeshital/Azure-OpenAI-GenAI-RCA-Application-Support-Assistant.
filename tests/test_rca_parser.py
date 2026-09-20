from app.rca_engine import parse_model_output


def test_parser():

    text = """
    Probable Root Cause

    Request throttling due to traffic pressure.

    Evidence

    - repeated 429 responses

    Immediate Actions

    - inspect request and token rate

    Validation Steps

    - monitor success rate

    Preventive Actions

    - review capacity
    """

    result = parse_model_output(
        text
    )

    assert (
        "throttling"
        in result[
            "probable_root_cause"
        ].lower()
    )

    assert result["evidence"]

    assert result["immediate_actions"]
