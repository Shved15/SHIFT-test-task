from sqlalchemy import (Column, Date, Float, ForeignKey, Integer, MetaData,
                        String)
from sqlalchemy.orm import relationship

from src.database.database import Base

# Создание объекта метаданных
metadata = MetaData()


class DepartmentModel(Base):
    """Определение модели Отдела."""

    __tablename__ = "departments"
    metadata = metadata

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    employees = relationship("EmployeeModel", back_populates="department")
    salaries = relationship("SalaryModel", back_populates="department")


class EmployeeModel(Base):
    """Определение модели Сотрудника."""

    __tablename__ = "employees"
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    start_date = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("DepartmentModel", back_populates="employees")
    salaries = relationship("SalaryModel", back_populates="employee")


class SalaryModel(Base):
    """Определение модели Зарплаты."""

    __tablename__ = "salaries"
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    current_salary = Column(Float)
    next_salary = Column(Float, nullable=True)
    raise_date = Column(Date, nullable=True)

    department = relationship("DepartmentModel", back_populates="salaries")
    employee = relationship("EmployeeModel", back_populates="salaries")
