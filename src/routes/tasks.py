from fastapi import APIRouter
from fastapi.responses import HTMLResponse
router = APIRouter(
    prefix= "/tasks",
    tags= ["tasks"]
)

@router.get("/")
async def root(response_class=HTMLResponse):
    return {
        "tasks": [
            {
                "id": 1,
                "title": "Task 1",
                "description": "Description 1",
                "status": "todo"
            },
            {
                "id": 2,
                "title": "Task 2",
                "description": "Description 2",
                "status": "in_progress"
            },
            {
                "id": 3,
                "title": "Task 3",
                "description": "Description 3",
                "status": "done"
            },
            {
                "id": 4,
                "title": "Task 4",
                "description": "Description 4",
                "status": "done"
            }
        ]
    }

