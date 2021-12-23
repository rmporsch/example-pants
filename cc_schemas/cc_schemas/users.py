from pydantic import BaseModel, UUID4


class User(BaseModel):
    name: str
    user_id: UUID4
