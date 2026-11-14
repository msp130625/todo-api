from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="To-Do API")


class TaskIn(BaseModel):
    title: str


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


# Tasks live in memory for now; they disappear when the app restarts.
tasks: dict[int, Task] = {}
next_id = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return list(tasks.values())


@app.post("/tasks", status_code=201)
def create_task(task_in: TaskIn) -> Task:
    global next_id
    task = Task(id=next_id, title=task_in.title)
    tasks[next_id] = task
    next_id += 1
    return task


@app.post("/tasks/{task_id}/complete")
def complete_task(task_id: int) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id].done = True
    return tasks[task_id]


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]