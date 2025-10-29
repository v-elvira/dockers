from flask import Flask
import os
import logging

app = Flask(__name__)

logging.basicConfig(
    filename='/data/logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.route("/")
def index():
    app.logger.info('trying Accessed the index page WITH NO adding app volume (no rebuild, del -v $(pwd)/app.py:/home/webuser/app.py).')
    return "trying Hello from a health-checked Flask WITH NO app volume again!"  # used v1 version of app.py from COPY (builded)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Логи можно писать в /data/logs, если хотите

    port = 5000
    app.run(host="0.0.0.0", port=port, debug=True)


# docker build -t flask-health .
# docker run --rm -p 5000:5000 --name fh -v $(pwd)/logs:/data/logs flask-health

# logs/app.log will be created and keep logs through container removes 

# docker run --rm -p 5000:5000 --name fh -v $(pwd)/logs:/data/logs -v $(pwd)/app.py:/home/webuser/app.py flask-health
# app volume for dev or not use it for prod (will be used v1 from image COPY instruction)
