from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/todos")


class Todo(BaseModel):
    id: int
    text: str
    done: bool = False


# In-memory storage for todos
todos: List[Todo] = []


@router.get("")
def list_todos():
    return todos


@router.post("")
def add_todo(todo: Todo):
    todos.append(todo)
    return todo


@router.put("/{todo_id}")
def update_todo(todo_id: int, updated: Todo):
    for idx, t in enumerate(todos):
        if t.id == todo_id:
            todos[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    for idx, t in enumerate(todos):
        if t.id == todo_id:
            del todos[idx]
            return {"deleted": todo_id}
    raise HTTPException(status_code=404, detail="Todo not found")
