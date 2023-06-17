from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud import get_employee
from src.database.config import (ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM,
                                 SECRET_KEY)
from src.database.database import get_db
from src.schemas.schemas import TokenData

SECRET_KEY = SECRET_KEY
ALGORITHM = ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)

# Создание схемы OAuth2PasswordBearer для получения токена доступа
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Метод создания токена доступа"""

    # Копирование данных и добавление времени истечения срока действия токена
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    # Создание токена доступа с использованием секретного ключа и алгоритма
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    """Получаем текущего пользователя на основе предоставленного токена доступа."""

    # Обработка ошибок аутентификации пользователя
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Декодирование токена и получение имени пользователя
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        # Создание объекта TokenData для передачи имени пользователя
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    # Получение пользователя из базы данных по имени пользователя
    user = await get_employee(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user
