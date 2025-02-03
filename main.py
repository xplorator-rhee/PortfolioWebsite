from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

blogs = [
    {"id": 1,
     "title": "Blueprints: The journey of self-taught full-stack",
     "date": "2025-02-02 20:17",
     "content": "Hello World!"
     }
]

app = FastAPI()
api_router = APIRouter()
app.mount("/static", StaticFiles(directory="static"), name="static")

@api_router.get("/", status_code=200)
def root() -> dict:
    return {"msg": "Hello World"}

@api_router.get("/musings/{blog_id}", status_code=200)
def fetch_blog(*, blog_id: int) -> dict:
    for blog in blogs:
        if blog["id"] == blog_id:
            result = blog
    return result["content"]

app.include_router(api_router)