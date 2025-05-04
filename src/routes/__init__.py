from fastapi import APIRouter

router = APIRouter(
    prefix="/tags",
    tags=["tasks"]
)

@router.get("/")
async def root():
    return {"message": "Hello World"}
