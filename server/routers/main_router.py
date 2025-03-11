from fastapi import APIRouter
from server.types import NicknameModel

router = APIRouter()

@router.get("/{nickname}")
async def main_root(nickname:str):
    try:
        validated = NicknameModel(nickname=nickname)
        
        
    except Exception as e:
        return {"error": str(e)}