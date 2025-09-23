from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to Secure SDLC Demo!"})

# Insecure example: vulnerable to XSS / injection
@app.route("/greet")
def greet():
    user_input = request.args.get("name", "")
    safe_input = re.sub(r'[^a-zA-Z0-9 ]', '', user_input)  # sanitize
    return jsonify({"greeting": f"Hello, {safe_input}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
