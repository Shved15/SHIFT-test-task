from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import EmployeeModel, SalaryModel
from src.schemas.schemas import SalaryCreate

# Создание объекта контекста шифрования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_employee(db: AsyncSession, username: str):
    """Получаем сотрудника из базы данных по его username"""

    return await db.run_sync(
        lambda session: session.query(EmployeeModel).filter(EmployeeModel.username == username).first())


async def authenticate_user(db: AsyncSession, username: str, password: str):
    """Аутентифицируем пользователя"""
    user = await get_employee(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user


async def get_salary_by_employee(db: AsyncSession, employee_id: int):
    """Получаем инфо о зарплате сотрудника по его ID."""
    return await db.run_sync(
        lambda session: session.query(SalaryModel).filter(SalaryModel.employee_id == employee_id).first())


async def create_salary(db: AsyncSession, salary_data: SalaryCreate):
    """Метод создания информации о зарплате сотрудника и даты следующего повышения"""
    new_salary = SalaryModel(**salary_data.dict())
    db.add(new_salary)
    await db.commit()
    await db.refresh(new_salary)
    return new_salary
