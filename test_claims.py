print("✅ test_claims.py started")

from src.components.claim_extractor import extract_claims
from src.components.consistency_checker import check_consistency

def main():
    print("🚀 Inside main()")

    backstory = """
    John grew up poor and never trusted authority.
    He was afraid of police officers.
    """

    narrative = """
    As an adult, John became a police officer and worked closely with law enforcement.
    He trusted his fellow officers.
    """

    claims = extract_claims(backstory)
    print("Extracted claims:")
    for c in claims:
        print("-", c)

    result = check_consistency(claims, narrative)

    print("\nFinal decision:", result["label"])
    if result["contradictions"]:
        print("Contradictions:")
        for c in result["contradictions"]:
            print("-", c)

if __name__ == "__main__":
    main()
