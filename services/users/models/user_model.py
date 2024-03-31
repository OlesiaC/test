from pydantic import BaseModel, field_validator
from datetime import datetime


class UserCreatedModel(BaseModel):
    """ Models for representing user data at different stages:"""

    id: int
    createdAt: datetime
    email: str
    username: str


    # Ensure ID and createdAt are not empty:
    @field_validator("id", "createdAt")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


# Model for full user details:
class UserFullModel(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    # Ensure all fields are not empty:
    @field_validator("id", "email", "first_name", "last_name", "avatar")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


# Model for storing updated timestamp:
class UserUpdatedModel(BaseModel):
    updatedAt: datetime  # Date and time of last update


# Response model for fetching a user by ID:
class GetUserByID(BaseModel):
    data: UserFullModel  # Nested model containing user details
