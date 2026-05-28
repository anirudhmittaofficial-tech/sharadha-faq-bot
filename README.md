# SharadhaStores AI Customer FAQ Bot

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your API Key
Create a `.env` file:
```
ANTHROPIC_API_KEY=your_api_key_here
```

Or export directly:
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### 3. Run locally
```bash
python app.py
```
Server runs at: `http://localhost:5000`

---

## API Endpoints

### GET /
Health check — confirms server is running.

### POST /chat
Send a customer question and get a reply.

**Request Body:**
```json
{
  "message": "What is the shelf life of Chakli?",
  "history": []
}
```

**Response:**
```json
{
  "reply": "Chakli has a shelf life of 30 days from the date of packing..."
}
```

**Multi-turn (with history):**
```json
{
  "message": "What about Besan Ladoo?",
  "history": [
    {"role": "user", "content": "What is the shelf life of Chakli?"},
    {"role": "assistant", "content": "Chakli has a shelf life of 30 days..."}
  ]
}
```

---

## Deploy on Render (Free)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add Environment Variable: `ANTHROPIC_API_KEY = your_key`
6. Deploy! You'll get a live URL like `https://sharadha-faq-bot.onrender.com`

---

## Project Structure
```
sharadha-faq-bot/
├── app.py              # Main Flask backend
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
└── README.md
```
