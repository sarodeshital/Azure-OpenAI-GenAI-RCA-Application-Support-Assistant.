from app.rag import retrieve


def test_retrieval_returns_documents():

    documents = retrieve(
        "429 throttling Azure OpenAI"
    )

    assert documents

    assert any(
        "429" in document["name"]
        for document in documents
    )
