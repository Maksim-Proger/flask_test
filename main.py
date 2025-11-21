from flask import Flask, request

app = Flask(__name__)

@app.route("/managed-object/config", methods=["POST"])
def managed_object_config():
    print("=== New request ===")
    print("Headers:", request.headers)
    print("Body:", request.get_data(as_text=True))
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
