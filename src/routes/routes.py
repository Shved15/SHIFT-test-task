from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.crud import get_salary_by_employee, authenticate_user
from src.database.database import get_db
from src.dependencies import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_user
from src.schemas.schemas import Token, Salary, Employee

router = APIRouter()


@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/salary/{employee_id}", response_model=Salary)
def read_salary(employee_id: int, db: Session = Depends(get_db),
                current_user: Employee = Depends(get_current_user)):
    if current_user.id != employee_id:
        raise HTTPException(status_code=400, detail="Not enough privileges")
    salary = get_salary_by_employee(db, employee_id=employee_id)
    if salary is None:
        raise HTTPException(status_code=404, detail="Salary not found")
    return salary
