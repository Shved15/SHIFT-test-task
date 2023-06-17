from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud import authenticate_user, get_salary_by_employee
from src.database.database import get_db
from src.dependencies import (ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token,
                              get_current_user)
from src.schemas.schemas import Employee, Salary, Token

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    """Post-запрос для получения токена доступа."""

    # Аутентификация пользователя
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Установка времени истечения срока действия токена доступа
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Создание токена доступа
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/salary/{employee_id}", response_model=Salary)
async def read_salary(employee_id: int, db: AsyncSession = Depends(get_db),
                      current_user: Employee = Depends(get_current_user)):
    """GET-запрос для получения текущей зарплаты и даты следующего повышения."""

    # Проверка прав доступа текущего пользователя
    if current_user.id != employee_id:
        raise HTTPException(status_code=400, detail="Not enough privileges")
    # Получение информации о зарплате сотрудника
    salary = await get_salary_by_employee(db, employee_id=employee_id)
    if salary is None:
        raise HTTPException(status_code=404, detail="Salary not found")
    return salary
