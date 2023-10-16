from fastapi import APIRouter

router = APIRouter()

@router.get("/users/",tags = ["users"])
def hello():
    return ["",""]