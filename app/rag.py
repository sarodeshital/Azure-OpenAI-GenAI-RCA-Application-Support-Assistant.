from pathlib import Path
import re

from .config import settings


KB_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "knowledge_base"
)


def tokenize(text):

    return set(
        re.findall(
            r"[a-zA-Z0-9]+",
            text.lower()
        )
    )


def lexical_similarity(query, document):

    query_tokens = tokenize(query)
    document_tokens = tokenize(document)

    if not query_tokens or not document_tokens:
        return 0.0

    return len(
        query_tokens.intersection(document_tokens)
    ) / len(query_tokens)


def load_documents():

    documents = []

    for path in sorted(KB_PATH.glob("*.md")):

        documents.append(
            {
                "name": path.name,
                "content": path.read_text(
                    encoding="utf-8"
                )
            }
        )

    return documents


def retrieve(query, top_k=None):

    top_k = top_k or settings.top_k

    documents = load_documents()

    ranked = sorted(
        documents,
        key=lambda document:
            lexical_similarity(
                query,
                document["content"]
            ),
        reverse=True
    )

    return ranked[:top_k]
