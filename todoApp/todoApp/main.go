package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/akhil/to-do/handler"
	"github.com/gorilla/mux"
)

func main() {
	initRouter()
}
func initRouter() {
	r := mux.NewRouter()
	r.HandleFunc("/todo", handler.CreateTodo).Methods(http.MethodPost)
	r.HandleFunc("/todo/{id}", handler.CreateTodo).Methods(http.MethodGet)
	r.HandleFunc("/todo/{userId}", handler.CreateTodo).Methods(http.MethodGet)
	r.HandleFunc("/todo", handler.CreateTodo).Methods(http.MethodDelete)

	fmt.Println("Server started on 8080 ")
	log.Fatal(http.ListenAndServe(":8080", r))
}
