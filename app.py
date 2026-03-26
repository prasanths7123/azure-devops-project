import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps from Azure 🚀"

if __name__ == "__main__":
    # Azure provides PORT dynamically
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)