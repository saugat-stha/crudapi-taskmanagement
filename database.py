import sqlite3

# Connect to SQLite (creates file if not exists)
conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

# Create tasks table if it doesn't exist
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'pending'
    )
    """)
    conn.commit()

# Function to insert a new task
def add_task(title, description):
    cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    conn.commit()

# Function to fetch all tasks
def get_all_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

# Function to fetch a single task by ID
def get_task_by_id(task_id):
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    return cursor.fetchone()

# Function to update a task
def update_task(task_id, title, description, status):
    cursor.execute("UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?", (title, description, status, task_id))
    conn.commit()

# Function to delete a task
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
