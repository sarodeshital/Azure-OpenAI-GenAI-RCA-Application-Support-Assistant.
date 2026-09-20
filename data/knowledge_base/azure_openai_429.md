# Azure OpenAI 429 Troubleshooting

HTTP 429 commonly indicates throttling or capacity/rate pressure.

## Investigate

1. Request rate.
2. Token consumption.
3. Concurrency.
4. Deployment capacity.
5. Quota.
6. Traffic changes.
7. Retry behavior.

## Important

Avoid uncontrolled retries because repeated requests can increase load.

## Immediate Mitigation

- Review request rate.
- Review token consumption.
- Review concurrency.
- Apply controlled retry/backoff where appropriate.
- Review capacity/quota.

## Validation

Monitor:

- success rate
- error rate
- latency
- request volume

## Prevention

Review capacity planning and application retry strategy.
