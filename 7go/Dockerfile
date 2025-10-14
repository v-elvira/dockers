FROM golang:1.20
WORKDIR /app
COPY main.go .
RUN go build -o app main.go
EXPOSE 8080
CMD ["./app"]
# = CMD ["/app/app"], quotes type matter: './app' is wrong! (/bin/sh: 1: [./app]: not found)
