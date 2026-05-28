from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is missing")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

# ─────────────────────────────────────────────
#  REAL SharadhaStores Knowledge Base
#  Source: https://www.sharadhastoresonline.com
# ─────────────────────────────────────────────
FAQ_KNOWLEDGE_BASE = """
SHARADHA STORES — AUTHENTIC HOMEMADE SOUTH INDIAN FOOD
Website: https://www.sharadhastoresonline.com
Store Address: 253, Alagiri Samy Salai, KK Nagar, Chennai, Tamil Nadu - 600078
Phone: 9884066779 / 9962796030
Email: gvijaydiya@gmail.com
Established: 1974
Payment: UPI (GPay, PhonePe, Paytm, 150+ UPI apps), Online payment

=== ABOUT THE STORE ===
Sharadha Stores is a well-known and trusted homemade food shop established in 1974 in Chennai.
They are known for authentic, traditional South Indian homemade products including:
Applams, Papads, Vattal, Vadam, Pickles, Rice Mix, Podi, Sweets, and Savories.
All products are 100% homemade with no artificial preservatives.

=== PRODUCT CATEGORIES ===

1. APPLAMS & PAPADS
   - Various types of homemade Applams (Appalam)
   - Papads in different flavors and sizes
   - Sun-dried, traditional preparation method

2. VATTAL & VADAM
   - Vattal (sun-dried vegetables)
   - Vadam (rice/sago-based crispy accompaniments)
   - Variety of flavors — plain, spicy, jeera, etc.
   - Traditionally made and sun-dried

3. PICKLES (Oorugai)
   - Homemade South Indian style pickles
   - Varieties include mango pickle, lemon pickle, mixed vegetable, etc.
   - Made with sesame oil and traditional spices
   - No artificial preservatives

4. RICE MIX (Sadam Mix / Ready Mix)
   - Instant Rice Mix Powders
   - Varieties: Tamarind Rice Mix, Lemon Rice Mix, Tomato Rice Mix, Coconut Rice Mix, Sambar Sadam Mix, etc.
   - Just mix with cooked rice — quick and easy

5. PODI (Dry Powder Condiments)
   - Idli Podi (Milagai Podi)
   - Dosa Podi
   - Rasam Powder
   - Sambar Powder
   - Curry Leaf Podi
   - Homemade with fresh spices

6. SWEETS (Mithai)
   - Traditional South Indian homemade sweets
   - Varieties: Besan Ladoo, Rava Ladoo, Coconut Burfi, Mysore Pak, Athirasam, etc.
   - Made with pure ghee and natural ingredients
   - Seasonal and festival specials available

7. SAVORIES (Snacks / Namkeen)
   - Murukku (various types)
   - Chakli
   - Ribbon Pakoda
   - Mixture
   - Thattai
   - Kara Boondi
   - Kai Murukku
   - All made fresh with rice flour, urad dal, and natural spices

=== SHELF LIFE ===
- Dry Snacks (Murukku, Chakli, Mixture, Thattai, Ribbon Pakoda): 30–45 days
- Applams & Papads: Up to 6 months (keep dry and airtight)
- Vattal & Vadam (unfried): 3–6 months in airtight container
- Pickles: 3–6 months; refrigerate after opening
- Rice Mix Powders: 2–3 months in airtight container
- Podi (Dry powders): 2–3 months in airtight container
- Sweets (Ladoo, Burfi): 15–20 days; refrigerate in summer
- Best consumed as soon as possible for freshness.
- Store all products in a cool, dry place, away from sunlight and moisture.

=== INGREDIENTS (General) ===
- All products are 100% vegetarian.
- Made with natural, homemade ingredients — no artificial colors, flavors, or preservatives.
- Applams/Papads: Urad dal flour, rice flour, salt, spices
- Vattal/Vadam: Rice, sago (sabudana), spices, sun-dried
- Pickles: Fresh vegetables/fruits, sesame oil (nallennai), mustard, red chili, salt
- Rice Mix: Tamarind, spices, curry leaves, groundnuts, sesame seeds (varies by type)
- Podi: Dry red chillies, urad dal, chana dal, curry leaves, asafoetida, salt
- Murukku/Chakli: Rice flour, urad dal flour, sesame seeds, butter, cumin, salt
- Sweets: Besan/rava, pure ghee, sugar, cardamom, dry fruits
- Products may contain groundnuts, sesame, gluten (wheat/urad dal). 
  Customers with allergies should contact the store directly.

=== DELIVERY ===
- Delivery available across India via courier.
- Minimum order amount: ₹500
- Actual delivery charges are applicable (charges vary by location and weight).
- Delivery time: Typically 3–7 business days depending on location.
- Orders dispatched after payment confirmation.
- Tracking details shared after dispatch.
- For delivery queries, contact: 9884066779 / 9962796030

=== ORDER & PAYMENT ===
- Order online at: https://www.sharadhastoresonline.com
- Payment via UPI (GPay, PhonePe, Paytm, and 150+ UPI apps).
- Online payment (cards, net banking) accepted.
- After ordering, you will receive confirmation and dispatch updates.
- For order status queries, contact the store with your order details.

=== BULK ORDERS ===
- Bulk orders available for weddings, festivals, corporate gifting, puja events.
- Traditional South Indian snacks and sweets are popular for festival gifting.
- Contact the store directly for bulk pricing and availability.
- Phone: 9884066779 / 9962796030
- Email: gvijaydiya@gmail.com
- Advance notice required for large bulk orders.

=== CONTACT & SUPPORT ===
- Phone: 9884066779 / 9962796030 (call or WhatsApp)
- Email: gvijaydiya@gmail.com
- Store Address: 253, Alagiri Samy Salai, KK Nagar, Chennai, Tamil Nadu - 600078
- Website: https://www.sharadhastoresonline.com
"""

SYSTEM_PROMPT = f"""You are a friendly and helpful customer support assistant for Sharadha Stores — 
an authentic homemade South Indian food brand established in 1974, based in Chennai.

You help customers with questions about:
- Products (applams, papads, vattal, vadam, pickles, rice mix, podi, sweets, savories)
- Ingredients and allergen information
- Shelf life and storage tips
- Delivery details and charges
- Order placement and order status
- Pricing (direct customers to the website for current prices)
- Bulk orders and gifting

Use only the information below to answer questions:

{FAQ_KNOWLEDGE_BASE}

Important guidelines:
1. Be warm, friendly, and helpful — like a genuine South Indian shopkeeper.
2. If asked about specific pricing, say prices vary by product and weight, and direct them to the website: https://www.sharadhastoresonline.com or ask them to call 9884066779.
3. If a question is outside the above topics (e.g. unrelated topics), politely redirect:
   "I can only help with questions about our products, delivery, ordering, and ingredients. For anything else, please call us at 9884066779 or email gvijaydiya@gmail.com."
4. Respond in the same language the customer uses — English, Tamil, Hindi, Kannada, or Telugu.
5. Keep answers concise and clear (2–5 sentences unless more detail is needed).
6. Never make up information not in the knowledge base.
7. End responses with "Is there anything else I can help you with?" when appropriate.
"""

# ─────────────────────────────────────────────
#  Routes
# ─────────────────────────────────────────────

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "🟢 Sharadha Stores FAQ Bot is running",
        "store": "Sharadha Stores — Authentic Homemade South Indian Food since 1974",
        "endpoints": {
            "POST /chat": "Send a customer question and get a reply",
            "GET /health": "Health check"
        }
    })


@app.route("/chat", methods=["POST"])
def chat():
    """
    Request:  { "message": "user question", "history": [...optional...] }
    Response: { "reply": "bot answer" }
    """
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Please provide a 'message' field."}), 400

    user_message = data["message"].strip()
    history = data.get("history", [])

    if not user_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    # Build full conversation
    messages = []
    for turn in history:
        if turn.get("role") in ("user", "assistant") and turn.get("content"):
            messages.append({"role": turn["role"], "content": turn["content"]})
    messages.append({"role": "user", "content": user_message})

    # Call Claude API
        # Call Claude API
    try:
        prompt = SYSTEM_PROMPT + "\n\nUser: " + user_message

        response = model.generate_content(prompt)

        reply = response.text

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# ─────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
