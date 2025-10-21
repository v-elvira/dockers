FROM python:3.9
RUN apt-get update && apt-get install -y nodejs npm
ENV APP_MODE=python PORT=8080
WORKDIR /app
ADD assets.tar.gz /app/assets
COPY requirements.txt package*.json flask_app.py node_app.js entrypoint.sh .
RUN pip install -r requirements.txt
RUN npm install
EXPOSE 8080
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
CMD []
