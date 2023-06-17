from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud import create_salary
from src.database.database import get_db
from src.schemas.schemas import Salary, SalaryCreate

# Создание маршрутизатора API для создания сотрудников
router = APIRouter(
    prefix="/salary",
    tags=['Salaries']
)


@router.post("/salary/", response_model=Salary)
async def create_salary_endpoint(salary: SalaryCreate, db: AsyncSession = Depends(get_db)):
    """Post-запрос на создание заработной платы сотрудника."""
    try:
        return await create_salary(db, salary)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
