from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_db
from src.models.models import EmployeeModel
from src.models.utils import Hash
from src.schemas.schemas import Employee, EmployeeCreate

# Создание маршрутизатора API для создания сотрудников
router = APIRouter(
    prefix="/employee",
    tags=['Employees']
)


@router.post('/', response_model=Employee)
async def create_employee(request: EmployeeCreate, db: AsyncSession = Depends(get_db)):
    """Post метод для создания нового сотрудника."""

    # Хеширование пароля с использованием класса Hash
    hashed_password = Hash.bcrypt(request.password)

    # Создание нового экземпляра модели EmployeeModel
    new_employee = EmployeeModel(username=request.username, email=request.email, phone_number=request.phone_number,
                                 first_name=request.first_name, last_name=request.last_name,
                                 start_date=request.start_date,
                                 department_id=request.department_id, hashed_password=hashed_password)

    # Добавление нового сотрудника в базу данных
    db.add(new_employee)
    await db.commit()
    await db.refresh(new_employee)
    return new_employee
