
# Test Plan

## Unit Testing

Test:

- error classification
- evidence generation
- retrieval
- RCA parsing

## Test Case 1 — 429

Input:

429

Expected:

Throttling classification.

---

## Test Case 2 — 401

Input:

401

Expected:

Authentication classification.

---

## Test Case 3 — 403

Input:

403

Expected:

Authorization classification.

---

## Test Case 4 — 404

Input:

404

Expected:

Resource/Deployment classification.

---

## Test Case 5 — RAG Quality

Input:

Incorrect answer.

Expected:

Investigate retrieved context before assuming model-generation failure.

---

## Test Case 6 — Missing Configuration

Expected:

Controlled configuration error.
