# Sharadha Stores AI Customer Support Chatbot

An AI-powered customer support chatbot for **Sharadha Stores**, a homemade South Indian food brand established in 1974.
Built using **Flask**, **Gemini AI**, **Render**, and **Vercel** with a modern responsive UI.

---

## 🚀 Features

* AI-powered customer support chatbot
* Answers product-related queries instantly
* Provides:

  * Product information
  * Shelf-life details
  * Ingredients
  * Delivery information
  * Bulk order support
* Responsive modern UI
* Cloud deployed frontend & backend
* Gemini AI integration

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript
* Vercel Deployment

### Backend

* Flask
* Flask-CORS
* Gemini API (Google Generative AI)
* Render Deployment

---

# 📂 Project Structure

```bash
sharadha-faq-bot/
│
├── app.py
├── requirements.txt
├── README.md
│
└── frontend/
    └── index.html
```

---

# ⚙️ Setup & Run Locally

## 1. Clone Repository

```bash
git clone https://github.com/anirudhmittaofficial-tech/sharadha-faq-bot.git
cd sharadha-faq-bot
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Set Environment Variable

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Or export directly:

```bash
export GEMINI_API_KEY=your_api_key_here
```

---

## 4. Run Backend

```bash
python app.py
```

Backend runs at:

```bash
http://localhost:5000
```

---

# 🔌 API Endpoints

## GET /

Health check endpoint.

### Response

```json
{
  "status": "running"
}
```

---

## GET /health

Backend health verification.

### Response

```json
{
  "status": "ok"
}
```

---

## POST /chat

Send customer queries and receive AI-generated responses.

### Request Body

```json
{
  "message": "What is the shelf life of Murukku?"
}
```

### Response

```json
{
  "reply": "Murukku typically has a shelf life of 30–45 days when stored in an airtight container."
}
```

---

# ☁️ Deployment

## Backend Deployment (Render)

1. Push project to GitHub
2. Go to Render
3. Create a New Web Service
4. Connect GitHub repository
5. Set:

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

6. Add Environment Variable:

```env
GEMINI_API_KEY=your_api_key
```

7. Deploy 🚀

---

## Frontend Deployment (Vercel)

1. Push frontend folder to GitHub
2. Import project in Vercel
3. Set Root Directory:

```bash
frontend
```

4. Deploy 🚀

---

# 🌐 Live Demo

## Frontend

https://sharadha-faq-bot-ftyl-2kz8d4qqt.vercel.app

---

# 👨‍💻 Developer

**Anirudh Sai Eswar Mitta**

* B.Tech CSE (Generative AI)
* Full Stack & AI Developer
* Passionate about AI-powered web applications

---

# 📜 License

This project is created for educational and portfolio purposes.
