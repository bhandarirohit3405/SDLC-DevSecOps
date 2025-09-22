**“Developing a Secure Software Development Lifecycle (SDLC) Framework for DevSecOps”** with a sample Python app, STRIDE threat modeling, secure coding, and a GitHub Actions pipeline integrated with Bandit (and optionally SonarCloud, pip-audit, OWASP ZAP, etc.).

# 📂 Project Structure

```
secure-sdlc-devsecops/
│── app/
│   └── app.py                 # Sample Python app
│   └── requirements.txt       # Dependencies
│── tests/
│   └── test_app.py            # Unit tests
│── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions pipeline
│── threat_model/
│   └── stride-diagram.png     # Threat modeling diagram (draw.io export)
│── README.md                  # Project documentation
│── .gitignore
│── LICENSE
```

---

# 🐍 Sample Python App (`app/app.py`)

```python
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
```

---

# 📦 Dependencies (`app/requirements.txt`)

```
flask==2.3.2
pytest==7.4.2
bandit==1.7.9
```

---

# 🧪 Unit Test (`tests/test_app.py`)

```python
import json
from app import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "Welcome" in data["message"]

def test_greet():
    client = app.test_client()
    response = client.get("/greet?name=Atul")
    data = json.loads(response.data)
    assert "Hello, Atul" in data["greeting"]
```

---

# ⚡ GitHub Actions Pipeline (`.github/workflows/ci.yml`)

```yaml
name: Secure SDLC CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          pip install -r app/requirements.txt

      - name: Run unit tests
        run: |
          pytest tests/

      - name: Run Bandit security scan
        run: |
          bandit -r app/ --exit-zero
```

---

# 📝 Steps to Run Locally

1. **Clone Repo**

   ```bash
   git clone https://github.com/<your-username>/secure-sdlc-devsecops.git
   cd secure-sdlc-devsecops/app
   ```

2. **Create Virtual Env & Install Dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

   pip install -r requirements.txt
   ```

3. **Run App**

   ```bash
   python app.py
   ```

   Access at 👉 [http://localhost:5000](http://localhost:5000)

4. **Run Unit Tests**

   ```bash
   pytest tests/
   ```

5. **Run Bandit Security Scan**

   ```bash
   bandit -r app/
   ```

---

# 📊 Threat Modeling (STRIDE)

* **Spoofing** → Validate inputs & authentication.
* **Tampering** → Sanitize user inputs (regex filter).
* **Repudiation** → Enable Flask logging.
* **Information Disclosure** → Avoid debug=True in production.
* **Denial of Service** → Rate limiting (Flask-Limiter, optional).
* **Elevation of Privilege** → Principle of Least Privilege for deployment.

Export diagrams from **draw\.io** and store them in `/threat_model/`.

---

# ✅ Expected Deliverables

* Working **Python app with secure coding practices**
* **GitHub Actions pipeline** enforcing tests + security checks
* **STRIDE-based threat model diagram**
* **README.md** explaining methodology, scope, and outcomes

---
