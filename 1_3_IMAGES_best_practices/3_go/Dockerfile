FROM golang:1.19

ENV APP_HOME=/app
ENV PORT=8080

WORKDIR /app
COPY main.go .

# RUN go get ./...  # what was it ?

RUN go build -o app /app/main.go

EXPOSE 8080
CMD ["go", "run", "main.go"]
# CMD ["./app"]
