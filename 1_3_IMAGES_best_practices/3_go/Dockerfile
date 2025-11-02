FROM golang:1.19

ENV APP_HOME=/app
ENV PORT=8080

WORKDIR /app
COPY main.go .

# RUN go get -u ./...  # = go get -u all (Upgrade all packages) 

EXPOSE 8080

## v1 (dev way, compiles into temp dir and runs):
# CMD ["go", "run", "main.go"]        

## v2:
RUN go build -o app /app/main.go
CMD ["./app"]
