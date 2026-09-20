# Azure OpenAI 401 Troubleshooting

HTTP 401 generally indicates an authentication problem.

## Checks

1. API key or access token validity.
2. Azure OpenAI endpoint.
3. Token acquisition.
4. Token expiration.
5. Environment variables.
6. Authentication configuration.

## Evidence

Collect:

- timestamp
- endpoint
- authentication method
- request/correlation identifier
- recent credential changes

Never expose credentials or API keys in logs.
