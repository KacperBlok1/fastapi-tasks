from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Tasks API")


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    done: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    done: bool | None = None


class Task(TaskCreate):
    id: int


tasks: list[Task] = []
next_id = 1

@app.get("/health", summary="Healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_in: TaskCreate):
    global next_id
    task = Task(id=next_id, **task_in.dict())
    tasks.append(task)
    next_id += 1
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_in: TaskUpdate):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_data = task.dict()
            update_fields = task_in.dict(exclude_unset=True)
            updated_data.update(update_fields)
            updated_task = Task(**updated_data)
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")