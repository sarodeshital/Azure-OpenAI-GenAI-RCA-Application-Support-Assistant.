# RAG Quality Troubleshooting

If an LLM answer is incorrect, separate retrieval quality from generation quality.

## Investigate Retrieval

1. Retrieved documents.
2. Chunking.
3. Embeddings.
4. Index configuration.
5. Search query.
6. Top-K.
7. Metadata filters.
8. Data freshness.

## Investigation Rule

If the correct context was not retrieved:

Investigate the retrieval pipeline.

If the correct context was retrieved but the answer is still incorrect:

Investigate prompt construction and generation behavior.

Do not automatically blame the LLM.
