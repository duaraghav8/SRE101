# syntax=docker/dockerfile:1
FROM golang:1.22

WORKDIR /src

COPY . .

RUN CGO_ENABLED=0 go build -o /app .

EXPOSE 8000
CMD ["/app"]
