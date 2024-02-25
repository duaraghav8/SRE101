package main

import (
    "fmt"
    "log"
    "net/http"
)

// controller definitions
func ping(w http.ResponseWriter, r *http.Request) {
    fmt.Println("/ping endpoint was invoked")
    fmt.Fprintf(w, "PONG")
}

func hello(w http.ResponseWriter, r *http.Request) {
    fmt.Println("/hello endpoint was invoked")
    fmt.Fprintf(w, "HELLO WORLD!!")
}

func main() {
    // register the endpoints
    http.HandleFunc("/ping", ping)
    http.HandleFunc("/hello", hello)

    // start the server, listen on localhost port 8000
    fmt.Println("Raghav's server is now running")
    log.Fatal(http.ListenAndServe(":8000", nil))
}
