from pydantic import BaseModel, Field

class NicknameModel(BaseModel):
    nickname: str = Field(..., description="Insta nickname", max_length=20, min_length=5)