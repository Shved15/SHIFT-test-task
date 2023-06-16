from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.models.models import EmployeeModel
from src.models.utils import Hash
from src.schemas.schemas import Employee, EmployeeCreate

# to ensure only the admin can add employees

router = APIRouter(
    prefix="/employee",
    tags=['Employees']
)


@router.post('/', response_model=Employee)
def create_employee(request: EmployeeCreate, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password)
    new_employee = EmployeeModel(username=request.username, email=request.email, phone_number=request.phone_number,
                                 first_name=request.first_name, last_name=request.last_name,
                                 start_date=request.start_date,
                                 department_id=request.department_id, hashed_password=hashed_password)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee
