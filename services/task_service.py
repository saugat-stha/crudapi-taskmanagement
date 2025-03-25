from db.database import add_task_to_db, get_all_tasks_from_db, get_task_from_db, update_task_in_db, delete_task_from_db
from models.task import TaskCreate, TaskUpdate

def create_task(task: TaskCreate):
    add_task_to_db(task.title, task.description)
    return {"message": "Task added successfully!"}

def get_tasks():
    tasks = get_all_tasks_from_db()
    return {"tasks": tasks}

def get_task(task_id: int):
    task = get_task_from_db(task_id)
    if task:
        return {"task": task}
    return {"error": "Task not found"}

def update_task(task_id: int, task: TaskUpdate):
    update_task_in_db(task_id, task.title, task.description, task.status)
    return {"message": "Task updated successfully!"}

def delete_task(task_id: int):
    delete_task_from_db(task_id)
    return {"message": "Task deleted successfully!"}
