from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table, add_task, get_all_tasks, get_task_by_id, update_task, delete_task

app = FastAPI()

# Create the tasks table (ensure it's created when the app starts)
create_table()

# Define Task Model for Request Body
class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: str
    description: str
    status: str

# Create a new task
@app.post("/tasks/")
def create_task(tasks: TaskCreate):
    add_task(tasks.title, tasks.description)
    return {"message": "Task added successfully!"}

# Get all tasks
@app.get("/tasks/")
def get_tasks():
    tasks = get_all_tasks()
    return {"tasks": [{"id": t[0], "title": t[1], "description": t[2], "status": t[3]} for t in tasks]}

# Get a single task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if task:
        return {"id": task[0], "title": task[1], "description": task[2], "status": task[3]}
    return {"error": "Task not found"}

# Update a task
@app.put("/tasks/{task_id}")
def update_task_endpoint(task_id: int, tasks: TaskUpdate):
    update_task(task_id, tasks.title, tasks.description, tasks.status)
    return {"message": "Task updated successfully!"}

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int):
    delete_task(task_id)
    return {"message": "Task deleted successfully!"}
