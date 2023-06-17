from passlib.context import CryptContext

# Создание объекта контекста шифрования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def bcrypt(password: str):
        # Хеширование пароля
        return pwd_context.hash(password)
