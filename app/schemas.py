from pydantic import BaseModel, EmailStr,ConfigDict

class UserCreate(BaseModel):
    id:int
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)
