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
    fmt.Println("Hello server is now running")
    log.Fatal(http.ListenAndServe(":8000", nil))
}

func main() {
    handleRequests()
}
