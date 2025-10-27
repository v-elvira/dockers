FROM nginx:alpine
# RUN apk add --no-cache bash
STOPSIGNAL SIGQUIT
SHELL ["/bin/bash", "-c"]

HEALTHCHECK --interval=30s CMD curl -f http://localhost/health.html  
# docker ps => healthy (or unhealthy if file not found) run and renew every 30s

# HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
#   CMD curl -f http://localhost/health.html || exit 1

COPY index.html /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/health.html
