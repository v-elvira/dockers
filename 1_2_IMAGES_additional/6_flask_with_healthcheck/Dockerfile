FROM python:3.9
RUN apt-get update && apt-get install -y curl
RUN useradd -m webuser
WORKDIR /home/webuser  # /home/webuser/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -f http://localhost:5000/health
VOLUME /data/logs
# USER webuser  # Permission denied: '/data/logs/app.log', the same if moved to /home/webuser/data/logs.app.log
CMD ["python", "app.py"]
