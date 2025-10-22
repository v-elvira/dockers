FROM alpine:3.17
RUN apk add --no-cache curl
COPY entrypoint.sh /app/entrypoint.sh
ENV PING_URL="https://example.com"
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["sh", "/app/entrypoint.sh"]