# Azure OpenAI 5xx Troubleshooting

5xx errors can indicate transient service-side or dependency problems.

## Investigate

1. Exact HTTP status code.
2. Timestamp.
3. Application logs.
4. Request/correlation identifiers.
5. Service health.
6. Network.
7. Gateway.
8. Dependencies.
9. Recent application changes.

Determine whether the failure is transient before applying retries.
