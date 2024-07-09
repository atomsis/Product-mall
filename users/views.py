from users.shemas import CreateUser
from fastapi import APIRouter
from users import crud
router = APIRouter(tags=['users',],prefix='/users')

@router.post('/')
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
