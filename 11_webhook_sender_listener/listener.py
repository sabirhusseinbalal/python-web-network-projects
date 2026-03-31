from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()  # Get JSON data from POST
    if data and "message" in data:
        print(f"Received message: {data['message']}")
    else:
        print("Received empty or invalid data")
    return {"status": "ok"}, 200  # Respond back

if __name__ == "__main__":
    print("Webhook Listener running on http://127.0.0.1:5000/webhook")
    app.run(debug=False)  # Set debug=False for production-like behavior