from fastapi import FastAPI, WebSocket, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from pyngrok import ngrok
import uvicorn
import nest_asyncio
import asyncio
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

# Retrieve the NGROK_AUTH_TOKEN variable from the environment
ngrok_auth_token = os.getenv('NGROK_AUTH_TOKEN')

nest_asyncio.apply()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

class SliderValue(BaseModel):
    value: int

current_value = 0
clients: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            global current_value
            current_value = int(data)
            for client in clients:
                await client.send_text(data)
    except Exception as e:
        clients.remove(websocket)

@app.get("/admin")
async def get_admin_page(request: Request):
    print(ws_url)
    return templates.TemplateResponse("admin.html", {"request": request, "ws_url": ws_url})

@app.get("/")
async def get_client_page(request: Request):
    print(ws_url)
    return templates.TemplateResponse("client.html", {"request": request, "ws_url": ws_url})

@app.get("/value")
def get_value():
    return {"value": current_value}

# Apply asyncio patch
nest_asyncio.apply()

# Authenticate ngrok
ngrok.set_auth_token(ngrok_auth_token)

# Start ngrok tunnel
public_url = ngrok.connect(8000, "http")
# public_url = "http://localhost:8000"
print('Public URL:', public_url)
public_url = public_url.public_url
ws_url = public_url
ws_url=ws_url+"/ws"
# Run the FastAPI app
uvicorn.run(app, host="0.0.0.0", port=8000)
