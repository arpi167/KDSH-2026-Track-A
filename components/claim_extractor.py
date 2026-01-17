import re

def extract_claims(backstory: str):
    """
    Extract simple factual and trait-based claims from backstory text.
    Returns a list of claims (strings).
    """
    claims = []

    sentences = re.split(r"[.!?]\s+", backstory)

    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue

        # Very simple heuristics (good enough for hackathon)
        if any(word in sent.lower() for word in [
            "never", "always", "grew up", "raised", "hates",
            "loves", "does not", "cannot", "afraid", "trauma"
        ]):
            claims.append(sent)

    return claims
