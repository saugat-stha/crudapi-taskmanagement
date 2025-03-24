
### Prerequisites

- Python 3.7+
- SQLite (comes pre-installed with Python)

### Install Dependencies

To get started, clone the repository and install the required dependencies:

```
pip install -r requirements.txt
```

### Run the FastAPI app with Uvicorn:

```
uvicorn main:app --reload
```

The server will be available at http://127.0.0.1:8000.

### API Endpoints
1. Create a Task
POST /tasks/


2. Get All Tasks
GET /tasks/

3. Get a Task by ID
GET /tasks/{task_id}

4. Update a Task
PUT /tasks/{task_id}

5. Delete a Task
DELETE /tasks/{task_id}

### Testing the API
You can test the API directly through the interactive Swagger UI that FastAPI provides:

### Open the browser and navigate to: 
http://127.0.0.1:8000/docs

From there, you can test all the CRUD operations.
