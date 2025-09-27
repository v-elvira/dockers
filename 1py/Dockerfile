FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
ENTRYPOINT ["python", "app.py"]
EXPOSE 8000