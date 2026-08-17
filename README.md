Here's a complete GitHub README for your University Library Chatbot project, now with an attractive banner at the top. The README is provided in a single, ready-to-copy markdown block.

---

```markdown
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
   ```

2. **Install Python dependencies**:
   ```bash
   pip install ollama
   # For web UI:
   pip install streamlit
   ```

3. **Pull the TinyLlama model** (or any model you prefer):
   ```bash
   ollama pull tinyllama
   ```

4. **Run the chatbot** (CLI):
   ```bash
   python library_chatbot.py
   ```

   Or run the Streamlit web app:
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
university-library-chatbot/
├── library_data.py          # Mock book database and user data
├── library_functions.py     # Core library operations (search, renew, etc.)
├── intent.py                # Rule-based intent detection
├── library_chatbot.py       # CLI chatbot entry point
├── app.py                   # Streamlit web UI (optional)
└── README.md
```

## 💻 Usage

### Command Line Interface

Run `python library_chatbot.py`. You will be greeted with:

```
📚 University Library Chatbot (type 'exit' to quit)
--------------------------------------------------
You:
```

Type your queries. Examples:

```
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
```

### Web Interface (Streamlit)

If you run the Streamlit app, you'll get a chat interface in your browser. The same logic applies; the UI shows a chat history and accepts input.

## 🔍 How It Works

1. **Intent Detection** (`intent.py`): Uses regular expressions to match user input against patterns for known intents. If no pattern matches, it returns `"llm"`.

2. **Library Functions** (`library_functions.py`): Contains functions that operate on the mock database:
   - `search_books(query)` – searches by title or author.
   - `get_availability(book_id)` – returns availability string.
   - `get_borrowed_books()` – lists borrowed books.
   - `get_fines()` – returns fines.
   - `renew_book(book_title)` – extends due date by 14 days.
   - `get_library_hours()` – returns opening hours.
   - `get_general_info()` – general help.

3. **Main Loop** (`library_chatbot.py`):
   - Takes user input.
   - Detects intent.
   - If intent is known, calls the appropriate library function and prints the result.
   - If intent is unknown, constructs a conversation history and queries the Ollama LLM (TinyLlama) for a response.

4. **Mock Data** (`library_data.py`): Contains a list of books (title, author, ISBN, location, total/available copies) and a single user with borrowed books and fines.

## 🧩 Customization

- **Change the LLM model**: Replace `MODEL = "tinyllama"` in `library_chatbot.py` with any model you have pulled in Ollama (e.g., `"phi3:mini"`, `"llama3.2:3b"`).
- **Expand the database**: Add more books to the `books` list in `library_data.py`.
- **Add new intents**: Extend the regex patterns in `intent.py` and add corresponding handling in `library_chatbot.py`.
- **Integrate a real database**: Replace the mock list with SQLite or PostgreSQL.

## 🚀 Future Improvements

- Implement fuzzy matching or NER for better book title extraction.
- Add user authentication and multi-user support.
- Include more intents (e.g., study room booking, library policies).
- Use a larger LLM for more accurate open-ended answers.
- Add logging and error handling.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (you may need to add one).
```

---

The banner uses a high-quality library image from Unsplash. Feel free to replace the image URL with your own custom banner if you have one. Let me know if you'd like any further adjustments!
