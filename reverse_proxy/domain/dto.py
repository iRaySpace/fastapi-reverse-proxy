from pydantic import BaseModel, Field

class LoginDto(BaseModel):
    username: str = Field()
    password: str = Field()
