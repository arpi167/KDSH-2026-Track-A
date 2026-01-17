import numpy as np
import pathway as pw


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    Compute cosine similarity between two vectors
    """
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def add_embeddings(table, embed_model):
    """
    Add embeddings column to a Pathway table
    """

    def embed_text(text: str):
        return embed_model.encode(text).tolist()

    return table.select(
        book_id=pw.this.book_id,
        text=pw.this.text,
        embedding=pw.apply(embed_text, pw.this.text),
    )


def retrieve_top_k(query, embedded_table, embed_model, k=3):
    """
    Retrieve top-k most relevant chunks using cosine similarity
    """

    # Encode query
    query_vec = embed_model.encode(query)

    # ✅ Execute Pathway graph
    pw.run()

    # ✅ Convert Pathway table to Pandas (stable API)
    df = embedded_table.to_pandas()

    results = []
    for _, row in df.iterrows():
        score = cosine_similarity(
            query_vec,
            np.array(row["embedding"])
        )
        results.append({
            "book_id": row["book_id"],
            "text": row["text"],
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:k]
