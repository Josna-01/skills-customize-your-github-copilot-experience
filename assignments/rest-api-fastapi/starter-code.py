from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Create FastAPI application
app = FastAPI(title="Task Management API", version="1.0.0")

# Pydantic model for task validation
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory task storage (for development)
tasks_db = [
    {"id": 1, "title": "Learn FastAPI", "description": "Understand FastAPI basics", "completed": False},
    {"id": 2, "title": "Build an API", "description": "Create a REST API", "completed": False},
]

# GET endpoint: Retrieve all tasks
@app.get("/tasks", response_model=List[Task])
async def get_tasks(completed: Optional[bool] = None):
    """
    Retrieve all tasks or filter by completion status.
    Query parameter: ?completed=true or ?completed=false
    """
    if completed is None:
        return tasks_db
    return [task for task in tasks_db if task["completed"] == completed]

# GET endpoint: Retrieve a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Retrieve a specific task by its ID."""
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# POST endpoint: Create a new task
@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: Task):
    """Create a new task."""
    # Check if ID already exists
    if any(t["id"] == task.id for t in tasks_db):
        raise HTTPException(status_code=400, detail="Task with this ID already exists")
    
    task_dict = task.dict()
    tasks_db.append(task_dict)
    return task_dict

# PUT endpoint: Update an existing task
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    """Update an existing task."""
    for i, existing_task in enumerate(tasks_db):
        if existing_task["id"] == task_id:
            updated_task = task.dict()
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# DELETE endpoint: Remove a task
@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    """Delete a task by its ID."""
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task not found")

# Root endpoint
@app.get("/")
async def root():
    """Welcome endpoint."""
    return {"message": "Welcome to Task Management API"}
