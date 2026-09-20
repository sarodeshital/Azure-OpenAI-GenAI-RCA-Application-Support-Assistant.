# GenAI Latency Troubleshooting

When response time increases, isolate the latency layer.

Measure:

- API request duration
- Azure OpenAI response time
- RAG retrieval time
- network time
- application processing time
- token volume
- timeout count
- retry count

Compare normal and degraded periods.

Check recent deployments and configuration changes.

The objective is to determine whether the bottleneck is:

Application
→ Network
→ Retrieval
→ Azure OpenAI
→ Dependency
