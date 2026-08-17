# library_chatbot.py
import re

try:
    import ollama
except ImportError:
    ollama = None

from intent import detect_intent
import library_functions as lib


MODEL = "tinyllama"

SYSTEM_PROMPT = (
    "You are a helpful university library assistant. "
    "Answer concisely and politely."
)


def _add_message(messages, role, content, limit=8):
    """
    Add a message to conversation history and keep only the latest messages.
    """
    messages = list(messages) + [{"role": role, "content": content}]
    return messages[-limit:]


def _call_llm(messages):
    """
    Call Ollama chat model safely.
    """
    if ollama is None:
        return (
            "Sorry, the ollama package is not installed. "
            "Run: pip install ollama"
        )

    try:
        response = ollama.chat(model=MODEL, messages=messages)

        # Supports both dictionary-style and object-style responses
        if hasattr(response, "message"):
            content = getattr(response.message, "content", "")
            return str(content).strip()

        return str(response["message"]["content"]).strip()

    except Exception as exc:
        return (
            f"Sorry, the local LLM is unavailable. "
            f"Make sure Ollama is running and you have pulled '{MODEL}'. "
            f"Details: {exc}"
        )


def handle_intent(intent, query):
    """
    Handle rule-based intents.
    Returns None if the query should be sent to the LLM.
    """
    if intent == "availability_or_search":
        results = lib.search_books(query)

        if results:
            response = ""

            for book in results[:3]:
                response += f"- {book['title']} by {book['author']} "
                response += f"(ISBN: {book['isbn']})\n"
                response += f"  {lib.get_availability(book['id'])}\n\n"

            return response.strip()

        return (
            "I couldn't find any books matching your query. "
            "Try providing the title, author, or ISBN."
        )

    elif intent == "renew":
        match = re.search(r"(?:renew|extend)\s+(.+)", query, re.IGNORECASE)

        if match:
            book_title = match.group(1).strip()
            return lib.renew_book(book_title)

        return "Which book would you like to renew? Please specify the title."

    elif intent == "borrowed":
        return lib.get_borrowed_books()

    elif intent == "fines":
        return lib.get_fines()

    elif intent == "hours":
        return lib.get_library_hours()

    elif intent == "general":
        return lib.get_general_info()

    else:
        # Fallback to LLM
        return None


def process_query(user_input, messages=None):
    """
    Main reusable function for CLI and Streamlit.
    Returns:
        response, updated_messages
    """
    if messages is None:
        messages = []

    user_input = user_input.strip()

    if not user_input:
        return "Please type a question.", messages

    messages = _add_message(messages, "user", user_input)

    intent = detect_intent(user_input)
    response = handle_intent(intent, user_input)

    if response is None:
        llm_messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ] + messages[-8:]

        response = _call_llm(llm_messages)

    messages = _add_message(messages, "assistant", response)

    return response, messages


def chat():
    """
    Command-line chatbot loop.
    """
    print("📚 University Library Chatbot (type 'exit' to quit)")
    print("--------------------------------------------------")

    messages = []

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input.strip():
            continue

        response, messages = process_query(user_input, messages)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    chat()