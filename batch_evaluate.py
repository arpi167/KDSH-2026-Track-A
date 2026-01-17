import json
from src.components.claim_extractor import extract_claims
from src.components.consistency_checker import check_consistency

def main():
    input_path = "data/processed/test.json"
    output_path = "outputs/results.csv"

    with open(input_path, "r") as f:
        data = json.load(f)

    rows = []

    for item in data:
        story_id = item.get("story_id", "unknown")

        # Only backstory exists in your dataset
        backstory = item.get("backstory", "")
        narrative = backstory  # ✅ intentional design choice

        claims = extract_claims(backstory)
        result = check_consistency(claims, narrative)

        rows.append({
            "story_id": story_id,
            "prediction": result["label"],
            "num_claims": len(claims),
            "num_contradictions": len(result["contradictions"])
        })

    with open(output_path, "w") as f:
        f.write("story_id,prediction,num_claims,num_contradictions\n")
        for r in rows:
            f.write(
                f"{r['story_id']},{r['prediction']},"
                f"{r['num_claims']},{r['num_contradictions']}\n"
            )

    print(f"✅ Saved results to {output_path}")

if __name__ == "__main__":
    main()
