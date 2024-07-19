# syntax=docker/dockerfile:1
FROM golang:1.22 AS build

WORKDIR /src

COPY go.mod go.mod
RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -o app .


# final stage (scratch image)
FROM scratch

COPY --from=build /src/app /app

EXPOSE 8000
CMD ["/app"]

