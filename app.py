import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    env_name = os.environ.get("ENVIRONMENT", "Development")
    return f"<h1>Hello from Cloud Run!</h1><p>Running in: <strong>{env_name}</strong></p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
