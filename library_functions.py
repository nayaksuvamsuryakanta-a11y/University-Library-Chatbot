# library_functions.py
import re
from datetime import datetime, timedelta
from library_data import books, user


STOP_WORDS = {
    "a", "an", "the", "please", "kindly", "can", "could", "would", "should",
    "i", "me", "my", "we", "our", "you", "your", "he", "she", "it", "they",
    "is", "are", "was", "were", "be", "been", "being", "am", "do", "does",
    "did", "have", "has", "had", "will", "shall", "may", "might", "must",
    "about", "of", "in", "on", "at", "to", "for", "with", "without", "and",
    "or", "but", "if", "then", "than", "so", "as", "by", "from", "into",
    "over", "under", "again", "further", "once", "here", "there", "when",
    "where", "why", "how", "what", "which", "who", "whom", "this", "that",
    "these", "those", "not", "no", "nor", "only", "own", "same", "s", "t",
    "don", "now", "book", "books", "library", "tell", "show", "give", "need",
    "want", "looking", "look", "find", "found", "search", "available",
    "availability", "locate", "location", "copy", "copies", "check", "checked",
    "out", "borrow", "borrowed", "renew", "extend", "due", "date", "fine",
    "fines", "hour", "hours", "open", "close", "help"
}


def _clean_text(text):
    """Lowercase text and remove punctuation."""
    if not text:
        return ""
    return re.sub(r"[^a-z0-9\s]", " ", text.lower()).strip()


def _get_keywords(text):
    """Extract useful keywords from user input."""
    words = _clean_text(text).split()
    return [word for word in words if word not in STOP_WORDS and len(word) > 1]


def search_books(query):
    """
    Search for books by title, author, or ISBN.
    Returns a list of matching books.
    """
    keywords = _get_keywords(query)

    if not keywords:
        return []

    scored_results = []

    for book in books:
        searchable_text = f"{book['title']} {book['author']} {book['isbn']}".lower()
        score = 0

        for keyword in keywords:
            if keyword in searchable_text:
                score += 1

        if score > 0:
            scored_results.append((score, book))

    scored_results.sort(key=lambda item: item[0], reverse=True)

    return [book for _, book in scored_results]


def get_availability(book_id):
    """Return availability string for a book."""
    for book in books:
        if book["id"] == book_id:
            if book["available_copies"] > 0:
                return (
                    f"{book['title']} is available "
                    f"({book['available_copies']} of {book['total_copies']} copies). "
                    f"Location: {book['location']}."
                )
            else:
                return (
                    f"{book['title']} is currently unavailable. "
                    f"Location: {book['location']}. All copies checked out."
                )

    return "Book not found."


def get_borrowed_books():
    """Return list of borrowed books with due dates."""
    result = []
    today = datetime.now().date()

    for item in user["borrowed_books"]:
        book = next((b for b in books if b["id"] == item["book_id"]), None)

        if book:
            try:
                due = datetime.strptime(item["due_date"], "%Y-%m-%d").date()
                status = "overdue" if due < today else "due"
                result.append(f"- {book['title']} ({status} {item['due_date']})")
            except ValueError:
                result.append(f"- {book['title']} (due {item['due_date']})")

    return "\n".join(result) if result else "No books currently borrowed."


def get_fines():
    """Return user's outstanding fines."""
    return f"Your outstanding fines total ₹{user['fines']:.2f}."


def renew_book(book_query):
    """
    Simulate renewing a book.
    Extends due date by 14 days.
    """
    keywords = _get_keywords(book_query)

    if not keywords:
        return "Which book would you like to renew? Please specify the title."

    cleaned_query = _clean_text(book_query)
    candidates = []

    for item in user["borrowed_books"]:
        book = next((b for b in books if b["id"] == item["book_id"]), None)

        if not book:
            continue

        cleaned_title = _clean_text(book["title"])
        title_words = cleaned_title.split()

        score = 0

        for keyword in keywords:
            if keyword in title_words:
                score += 1

        # Extra score if the cleaned query appears directly inside the title
        if cleaned_query and cleaned_query in cleaned_title:
            score += 2

        if score > 0:
            candidates.append((score, item, book))

    if not candidates:
        return "Book not found in your borrowed list."

    candidates.sort(key=lambda candidate: candidate[0], reverse=True)

    best_score = candidates[0][0]
    best_matches = [candidate for candidate in candidates if candidate[0] == best_score]

    if len(best_matches) > 1:
        titles = ", ".join(candidate[2]["title"] for candidate in best_matches)
        return (
            f"Multiple borrowed books match your request: {titles}. "
            f"Please specify the exact title."
        )

    _, item, book = best_matches[0]

    old_due = datetime.strptime(item["due_date"], "%Y-%m-%d")
    new_due = old_due + timedelta(days=14)
    item["due_date"] = new_due.strftime("%Y-%m-%d")

    return f"{book['title']} renewed. New due date: {item['due_date']}."


def get_library_hours():
    """Return library opening hours."""
    return (
        "Library hours: Mon-Fri 8:00 AM – 11:00 PM, "
        "Sat-Sun 10:00 AM – 6:00 PM."
    )


def get_general_info():
    """Return general information about the library assistant."""
    return (
        "This is the University Library assistant. "
        "You can ask about book availability, borrowing, renewals, fines, "
        "library hours, and more."
    )