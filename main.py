from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

# Start FastAPI
app = FastAPI()

# CORS configuration to allow the API to be accessed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Entity Models for Tasks
class Task(BaseModel):
    id: int
    title: str
    desc: Optional[str] = None
    completed: bool = False

class UpdateTask(BaseModel):
    title: Optional[str] = None
    desc: Optional[str] = None
    completed: Optional[bool] = None

# In-memory database
tasks = [
    {
        "id": 1766598791932,
        "title": "📌 Nota Importante",
        "desc": "Esta aplicação utiliza salvamento em memória (RAM). Se o servidor ficar inativo, os dados serão redefinidos.",
        "completed": False
    }
]

# List tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Create task
@app.post("/tasks")
def create_task(task: Task):
    new_task = task.dict() 
    tasks.append(new_task)
    return new_task

# Update the task by ID 
@app.put("/tasks/{taskId}")
def update_task(taskId: int, data: UpdateTask):
    for t in tasks:
        if t["id"] == taskId:
            if data.title is not None: t["title"] = data.title
            if data.desc is not None: t["desc"] = data.desc
            if data.completed is not None: t["completed"] = data.completed
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# Delete the task by ID
@app.delete("/tasks/{taskId}")
def delete_task(taskId: int):
    global tasks
    initial_count = len(tasks)
    tasks = [t for t in tasks if t["id"] != taskId]
    
    if len(tasks) == initial_count:
        raise HTTPException(status_code=404, detail="ID não encontrado na memória")
        
    return {"message": f"Tarefa {taskId} deletada com sucesso"}

# Start the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)