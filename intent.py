# intent.py
import re


def detect_intent(query):
    """
    Detect user intent using keyword and regex matching.
    """
    query = query.lower().strip()

    if not query:
        return "llm"

    # Renewal intent
    if re.search(r"\b(renew|extend)\b", query):
        return "renew"

    # Fines intent
    if re.search(
        r"\b(fines?|penalty|penalties|charges?|owe|owed|payment|pay|overdue)\b",
        query
    ):
        return "fines"

    # Borrowed books intent
    if re.search(
        r"\b(borrowed|checked\s*out|my books|my book|loan|loans|due|return\s+date)\b",
        query
    ):
        return "borrowed"

    # Library hours intent
    if re.search(
        r"\b(hours?|open|opens|close|closes|closed|timing|timings)\b",
        query
    ):
        return "hours"

    # Availability or search intent
    if re.search(
        r"\b("
        r"available|availability|find|locate|location|where|search|"
        r"look\s+for|copy|copies|isbn|title|author|have|has|holding|holdings"
        r")\b",
        query
    ):
        return "availability_or_search"

    # General help intent
    if re.search(r"\b(help|what can you do|services)\b", query):
        return "general"

    # Fallback to LLM
    return "llm"