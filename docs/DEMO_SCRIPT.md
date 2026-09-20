# Interview Demo Script

## Demo 1 — 429

Enter:

Incident ID:

INC-1001

Error:

429

Description:

Users report intermittent Azure OpenAI failures during peak traffic.

Show the logs.

Explain:

Repeated 429 responses indicate a possible throttling/capacity issue.

Then explain:

- request rate
- token consumption
- concurrency
- quota
- retry behavior

---

## Demo 2 — 401

Select:

401

Explain:

401 is primarily an authentication problem.

Check:

- credential
- token
- endpoint
- token expiration
- authentication configuration

---

## Demo 3 — Incorrect RAG Answer

Explain:

HTTP 200 does not guarantee a correct answer.

First inspect retrieved context.

If retrieval is wrong:

Investigate the RAG layer.

If retrieval is correct:

Investigate prompt and generation behavior.

---

## Final Interview Statement

This project is a portfolio simulation designed to demonstrate Azure OpenAI application-support concepts. It is not presented as production client experience.
