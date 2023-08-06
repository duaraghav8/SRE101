# syntax=docker/dockerfile:1
FROM golang:1.20
WORKDIR /src
ADD . .
RUN CGO_ENABLED=0 go build -o app .
EXPOSE 8000
CMD ["./app"]
