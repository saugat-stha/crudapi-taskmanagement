from fastapi import APIRouter
from models.task import TaskCreate, TaskUpdate
from services.task_service import create_task, get_tasks, get_task, update_task, delete_task

router = APIRouter()

@router.post("/tasks/")
def create_new_task(task: TaskCreate):
    return create_task(task)

@router.get("/tasks/")
def fetch_tasks():
    return get_tasks()

@router.get("/tasks/{task_id}")
def fetch_task(task_id: int):
    return get_task(task_id)

@router.put("/tasks/{task_id}")
def modify_task(task_id: int, task: TaskUpdate):
    return update_task(task_id, task)

@router.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    return delete_task(task_id)
