FROM python:3.9
RUN apt-get update && apt-get install -y curl
RUN pip install flask
WORKDIR /app
COPY script.py config.ini /app/
ENV LOG_LEVEL=info
ENV APP_MODE=production
EXPOSE 9000
CMD ["python", "/app/script.py"]
