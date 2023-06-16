from typing import Optional
from pydantic import BaseModel
from datetime import date


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# Модели для Отдела
class DepartmentBase(BaseModel):
    name: str


class DepartmentCreate(DepartmentBase):
    pass


class Department(DepartmentBase):
    id: int

    class Config:
        orm_mode = True


# Модели для Сотрудников
class EmployeeBase(BaseModel):
    username: str
    email: str
    phone_number: str
    first_name: str
    last_name: str
    start_date: date
    department_id: int


class EmployeeCreate(EmployeeBase):
    password: str


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True


# Модели для Зарплаты
class SalaryBase(BaseModel):
    employee_id: int
    department_id: int
    current_salary: float
    next_salary: Optional[float] = None
    raise_date: Optional[date] = None
    raise_percentage: Optional[float] = None


class SalaryCreate(SalaryBase):
    pass


class Salary(SalaryBase):
    id: int

    class Config:
        orm_mode = True
