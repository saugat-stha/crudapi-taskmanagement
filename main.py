from fastapi import FastAPI
from routes import task

app = FastAPI()

# Include the routes
app.include_router(task.router)