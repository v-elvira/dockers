from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Advanced Dockerfile!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
