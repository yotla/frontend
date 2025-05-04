from fastapi import FastAPI, Request, HTTPException, WebSocket, WebSocketDisconnect, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
import os
from pathlib import Path
from typing import Optional, Dict
from datetime import datetime
import json
import uvicorn
import sys

if not "" in sys.path:
    sys.path.insert(0, "")

from src.routes.tasks import router as tasks_router
from src.routes.site import router as site_router

from src.config import Config




# Create the FastAPI application
app = FastAPI(
    title="yotla-frontend"
    )

templates = Jinja2Templates(directory="src/templates")

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(tasks_router)
app.include_router(site_router)

@app.get("/")
async def root(request: Request):
    return RedirectResponse(url="/site")

if __name__ == "__main__":
    # Get host and port from environment variables or use defaults
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    
    # Start the Uvicorn server
    uvicorn.run(
        "src.main:app",
        host=host,
        port=port,
        reload=False,  # Enable auto-reload during development
        log_level="info"
    )
    
    print(f"Server running at http://{host}:{port}") 