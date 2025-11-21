from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True, silent=True)
    print("Received POST:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # host=0.0.0.0 — позволяет принимать запросы из сети
    app.run(host="0.0.0.0", port=5000)
