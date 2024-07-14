from fastapi import Path, APIRouter

router = APIRouter(
    tags=[
        "items",
    ],
    prefix="/items",
)


# @router.get("/latest/")
# def get_latest_item():
#     return {"latest items": fake_db[-2:]}


@router.get("/{item_id}")
def get_item(item_id: int = Path(ge=1, lt=1000000)):
    return {"item": {"id": item_id}}
