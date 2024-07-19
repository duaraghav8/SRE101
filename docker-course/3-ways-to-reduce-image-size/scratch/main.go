package main

import (
    "fmt"
    "log"
    "net/http"
)

func helloWorld(w http.ResponseWriter, r *http.Request){
    fmt.Fprintf(w, "Hello world!")
    fmt.Println("Endpoint Hit: helloWorld()")
}

func handleRequests() {
    http.HandleFunc("/", helloWorld)
    fmt.Println("HTTP server is now running on port 8000")
    log.Fatal(http.ListenAndServe(":8000", nil))
}

func main() {
    handleRequests()
}
