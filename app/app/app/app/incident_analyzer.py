ERROR_MAP = {
    "400": (
        "Bad Request",
        "Inspect request payload, required parameters and API schema."
    ),

    "401": (
        "Authentication",
        "Validate credential/token configuration and endpoint."
    ),

    "403": (
        "Authorization",
        "Validate identity, RBAC, resource access and network controls."
    ),

    "404": (
        "Resource/Deployment",
        "Validate endpoint, deployment name, resource and API path."
    ),

    "408": (
        "Timeout",
        "Inspect client timeout, service latency and dependencies."
    ),

    "429": (
        "Throttling",
        "Inspect request rate, token usage, concurrency, quota and retry behavior."
    ),

    "500": (
        "Server Error",
        "Inspect service response, dependencies and transient failures."
    ),

    "502": (
        "Bad Gateway",
        "Inspect gateway and upstream/downstream dependencies."
    ),

    "503": (
        "Service Unavailable",
        "Inspect service availability, dependencies and infrastructure."
    )
}


def classify_error(error_code: str):

    return ERROR_MAP.get(
        str(error_code),
        (
            "Unknown",
            "Collect logs, metrics and request context before isolating the failure."
        )
    )


def build_evidence(incident):

    evidence = [
        f"Incident error code: {incident.error_code}",
        f"Service: {incident.service}"
    ]

    if incident.logs:

        evidence.append(
            f"{len(incident.logs)} log entries supplied for analysis."
        )

        matching = [
            log
            for log in incident.logs
            if incident.error_code in log
        ]

        if matching:
            evidence.append(
                f"{len(matching)} log entries contain the incident error code."
            )

    return evidence
