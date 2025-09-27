#!/bin/sh
echo "Starting my new ping script..."

URL="${PING_URL:-http://google.com}"

while true
do
  echo "Pinging $URL..."
  curl -I $URL
  sleep 5
done
