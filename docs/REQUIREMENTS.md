# Software Requirements Specification

## Functional Requirements

### FR-01
The system shall accept an incident ID.

### FR-02
The system shall accept an application/service name.

### FR-03
The system shall accept an HTTP error code.

### FR-04
The system shall accept incident description and logs.

### FR-05
The system shall classify common application-support errors.

### FR-06
The system shall retrieve relevant troubleshooting knowledge.

### FR-07
The system shall use Azure OpenAI for RCA generation.

### FR-08
The system shall provide evidence.

### FR-09
The system shall provide immediate troubleshooting actions.

### FR-10
The system shall provide validation steps.

### FR-11
The system shall provide preventive actions.

### FR-12
The system shall expose a health endpoint.

## Non-Functional Requirements

- Secure secret management
- Input validation
- Logging
- Error handling
- Testability
- Maintainability
- Modular design
- Azure deployment readiness

## Out of Scope

- Autonomous production remediation
- Real customer data
- Real client credentials
- Production SLA claims
- Production incident claims
