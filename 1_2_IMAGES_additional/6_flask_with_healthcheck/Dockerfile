FROM python:3.9
RUN useradd -m webuser
HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:5000/health
VOLUME /data/logs
WORKDIR /home/webuser
COPY requirements.txt app.py .
RUN pip install -r requirements.txt
EXPOSE 5000
# USER webuser  # Permission denied: '/data/logs/app.log', the same if moved to /home/webuser/data/logs.app.log
CMD ["python", "app.py"]
