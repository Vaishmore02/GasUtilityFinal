package service

import (
	"time"

	"github.com/akhil/to-do/model"
	uuid "github.com/google/uuid"
)

func CreateTodo(todo model.TodoTask) (string, error) {
	//create new id & update timestamps
	todo.Id = uuid.New().String()
	todo.CreatedAt = time.Now()
	todo.UpdatedAt = time.Now()

	//add in db
	return todo.Id, nil
}
