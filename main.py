from fastapi import FastAPI

from src.routes import employee, salary
from src.routes.routes import router

app = FastAPI()

app.include_router(router)
app.include_router(employee.router)
app.include_router(salary.router)
