# Security

## Secrets

Never commit:

- API keys
- passwords
- tokens
- connection strings
- certificates
- customer data

## Local Development

Use `.env`.

## GitHub

Only commit:

`.env.example`

Never commit:

`.env`

## Production

For a production Azure implementation, use appropriate identity-based authentication, managed identity and secure secret-management mechanisms.

## Least Privilege

Grant only the permissions required by the application.

## Data

This portfolio uses synthetic/sample incidents.

## Human Approval

The application generates troubleshooting recommendations.

It does not automatically execute production remediation.
