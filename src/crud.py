from sqlalchemy.orm import Session
from passlib.context import CryptContext

from src.models.models import EmployeeModel, SalaryModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_employee(db: Session, username: str):
    return db.query(EmployeeModel).filter(EmployeeModel.username == username).first()


def authenticate_user(db: Session, username: str, password: str):
    user = get_employee(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user


def get_salary_by_employee(db: Session, employee_id: int):
    return db.query(SalaryModel).filter(SalaryModel.employee_id == employee_id).first()
