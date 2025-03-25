import sqlite3

# Create a connection to SQLite
conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

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

def add_task_to_db(title, description):
    cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    conn.commit()

def get_all_tasks_from_db():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def get_task_from_db(task_id):
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    return cursor.fetchone()

def update_task_in_db(task_id, title, description, status):
    cursor.execute("UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?",
                   (title, description, status, task_id))
    conn.commit()

def delete_task_from_db(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
