# syntax=docker/dockerfile:1
FROM golang:1.22

WORKDIR /src

# download dependencies
COPY go.mod go.mod
RUN go mod download

# copy source files into the image
COPY . .

# build the final executable
RUN CGO_ENABLED=0 go build -o /app .

# run the application
EXPOSE 8000
CMD ["/app"]
