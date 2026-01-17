from pathlib import Path
import pathway as pw


# -------------------------
# Schema definition
# -------------------------
class BookSchema(pw.Schema):
    book_id: str
    text: str


# -------------------------
# Pathway ingestion
# -------------------------
def build_pathway_table(data_dir: str = "data/raw/Books"):
    print("📚 Loading books from:", data_dir)

    rows = []
    books_path = Path(data_dir)

    if not books_path.exists():
        print(f"⚠️ Books directory not found: {data_dir}")
        return None

    for book_file in books_path.glob("*.txt"):
        try:
            text = book_file.read_text(encoding="utf-8", errors="ignore")

            # ✅ TUPLE format (order must match schema)
            rows.append(
                (
                    book_file.stem,  # book_id
                    text             # text
                )
            )

        except Exception as e:
            print(f"❌ Failed to read {book_file.name}: {e}")

    if not rows:
        print("⚠️ No books loaded")
        return None

    print(f"✅ Loaded {len(rows)} books")

    # ✅ CORRECT Pathway 0.28 API
    table = pw.debug.table_from_rows(
        BookSchema,
        rows
    )

    return table
