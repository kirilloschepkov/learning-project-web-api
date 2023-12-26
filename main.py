from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import models

from database import engine
from routes.posts import router_posts
from routes.subjects import router_subjects
from routes.websocket import router_websocket

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="templates"))

HOST = "0.0.0.0"
PORT = 8000

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "http_protocol": "https",
            "ws_protocol": "wss",
            "server_run": f'{HOST}:{PORT}'
        }
    )


app.include_router(router_websocket)
app.include_router(router_subjects)
app.include_router(router_posts)

if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=PORT, reload=True)
