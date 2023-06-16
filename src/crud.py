from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext

from src.models.models import EmployeeModel, SalaryModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_employee(db: AsyncSession, username: str):
    return await db.run_sync(
        lambda session: session.query(EmployeeModel).filter(EmployeeModel.username == username).first())


async def authenticate_user(db: AsyncSession, username: str, password: str):
    user = await get_employee(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user


async def get_salary_by_employee(db: AsyncSession, employee_id: int):
    return await db.run_sync(lambda session: session.query(SalaryModel).filter(SalaryModel.employee_id == employee_id).first())

