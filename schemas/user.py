from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(...,min_length=4)

class ShowUser(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    # class Config():
    #     orm_mode = True # to return json format

    model_config = ConfigDict(from_attributes=True)
