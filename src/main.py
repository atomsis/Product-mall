from fastapi import FastAPI
import uvicorn
from items_view import router as item_rout
from users.views import router as users_rout

app = FastAPI()

app.include_router(item_rout)
app.include_router(users_rout)


@app.get("/hello/")
def hello(name: str):
    name = name.strip()
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8888)
