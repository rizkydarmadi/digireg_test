from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# PostgreSQL database connection configuration
db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "zefanya",
    "host": "localhost",
    "port": "5463",
}

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_config)
except psycopg2.OperationalError as e:
    print(f"Error connecting to the PostgreSQL database: {e}")
    exit()

# Create a cursor to interact with the database
cursor = conn.cursor()

# Create the "todos" table if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        task TEXT
    )
    """
)
conn.commit()


class TodoItem(BaseModel):
    task: str


@app.get("/todos")
def get_todos():
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    todo_items = []
    for todo in todos:
        todo_items.append({"id": todo[0], "task": todo[1]})
    return todo_items


@app.get("/todos/{item_id}")
def get_todo_item(item_id: int):
    cursor.execute("SELECT * FROM todos WHERE id = %s", (item_id,))
    todo = cursor.fetchone()
    if todo is None:
        raise HTTPException(
            status_code=404, detail=f"TODO item {item_id} not found"
        )
    return {"id": todo[0], "task": todo[1]}


@app.post("/todos")
def create_todo_item(todo: TodoItem):
    try:
        cursor.execute(
            "INSERT INTO todos (task) VALUES (%s)",
            (todo.task,),
        )
        conn.commit()
        return {"message": "TODO item created successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


@app.put("/todos/{item_id}")
def update_todo_item(item_id: int, todo: TodoItem):
    try:
        cursor.execute(
            "UPDATE todos SET task = %s WHERE id = %s",
            (todo.task, item_id),
        )
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404, detail=f"TODO item {item_id} not found"
            )
        conn.commit()
        return {"message": f"TODO item {item_id} updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


@app.delete("/todos/{item_id}")
def delete_todo_item(item_id: int):
    try:
        cursor.execute("DELETE FROM todos WHERE id = %s", (item_id,))
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404, detail=f"TODO item {item_id} not found"
            )
        conn.commit()
        return {"message": f"TODO item {item_id} deleted successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
