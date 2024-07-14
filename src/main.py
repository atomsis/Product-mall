from fastapi import FastAPI
import uvicorn
from items_view import router as item_rout
from users.views import router as users_rout
from contextlib import asynccontextmanager
from core.models import Base, db_helper
from fastapi.routing import APIRouter
from api_v1 import router as router_v1
from pydantic import BaseModel
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)
app.include_router(item_rout)
app.include_router(users_rout)


@app.get("/hello/")
def hello(name: str):
    name = name.strip()
    return {"message": f"Hello {name}"}


@app.get("/test1/")
def test1():
    return {"message": "test1"}


@app.get("/test2/", openapi_extra={"x-aperture-labs-portal": "blue"})
def test2():
    return {"message": "test2"}


def use_route_name_as_oper(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRouter):
            route.operation_id = route.name


# use_route_name_as_oper(app)
@app.get("/test3/", operation_id="specific_id", include_in_schema=False)
def test3():
    return {"message": "test3"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8888)
