from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class DailySpending(BaseModel):
    daily_spending: int

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: int
    email: EmailStr
    monthly_salary: int

    class Config:
        orm_mode = True


class UserSpend(DailySpending):
    pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    monthly_salary: int


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    monthly_salary: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
