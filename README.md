<div align="center">
  <img src="https://images.unsplash.com/photo-1521587760476-6c12a4b040da?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1200&q=80" alt="University Library Chatbot Banner" width="100%" style="max-width: 800px; border-radius: 10px;">
  <h1>📚 University Library Chatbot</h1>
  <p><em>A hybrid chatbot combining rule-based logic with a local LLM for university library services.</em></p>
</div>

---

## ✨ Features

- 🔍 **Book Search** – Find books by title or author.
- 📅 **Availability** – Check real-time availability and location.
- 🔄 **Renewals** – Renew borrowed books with extended due dates.
- 💰 **Fines** – View outstanding fines.
- 🕒 **Library Hours** – Get opening/closing times.
- 💬 **Conversational Fallback** – For open-ended questions, the bot uses a local LLM to generate helpful responses.
- 🌐 **Optional Web UI** – Streamlit-based browser interface.

## 🧠 Approach

The bot uses a **hybrid architecture**:

1. **Rule-based intent detection** – Keyword matching and regex to identify common intents (search, availability, renew, fines, hours, general help). This ensures accurate, structured responses for routine queries.
2. **Local LLM (Ollama + TinyLlama)** – When the intent is not recognized, the query is passed to a small language model running locally, which provides a friendly, conversational answer.
3. **Mock database** – A Python list simulates the library catalogue and user data, making it easy to test without external dependencies.

This design demonstrates how to combine deterministic logic with generative AI for a reliable and extensible assistant.

## 🛠️ Technologies Used

- **Python 3.8+**
- **Ollama** – Local LLM runtime
- **TinyLlama** (or any Ollama-supported model) – Language model for fallback
- **Streamlit** (optional) – Web interface
- **Regex** – Intent detection

## 📋 Prerequisites

- [Ollama](https://ollama.com/) installed and running.
- Python 3.8+ with pip.
- `ollama` Python package: `pip install ollama`
- (Optional) `streamlit`: `pip install streamlit`

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/university-library-chatbot.git
   cd university-library-chatbot
   python library_chatbot.py
   university-library-chatbot/
├── library_data.py          # Mock book database and user data
├── library_functions.py     # Core library operations (search, renew, etc.)
├── intent.py                # Rule-based intent detection
├── library_chatbot.py       # CLI chatbot entry point
├── app.py                   # Streamlit web UI (optional)
└── README.md
📚 University Library Chatbot (type 'exit' to quit)
--------------------------------------------------
You:
You: Where can I find Clean Code?
Bot: - Clean Code by Robert C. Martin (ISBN: 978-0132350884)
  Availability: Clean Code is available (5 of 5 copies). Location: Floor 1, Section B, Shelf 5

You: Is Deep Learning available?
Bot: - Deep Learning by Ian Goodfellow (ISBN: 978-0262035613)
  Availability: Deep Learning is currently unavailable. Location: Floor 3, Section C, Shelf 20. All copies checked out.

You: What are my borrowed books?
Bot: - Introduction to Algorithms (due 2025-06-01)
- Deep Learning (due 2025-05-25)

You: Renew Introduction to Algorithms
Bot: Introduction to Algorithms renewed. New due date: 2025-06-15.

You: How much are my fines?
Bot: Your outstanding fines total ₹15.50.

You: What are the library hours?
Bot: Library hours: Mon-Fri 8:00 AM – 11:00 PM, Sat-Sun 10:00 AM – 6:00 PM.

You: Can you recommend a book on AI?
Bot: [LLM-generated response]
