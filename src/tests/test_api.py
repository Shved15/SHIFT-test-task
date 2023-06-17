import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_get_salary_after_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # логинимся что бы получить токен
        response = await ac.post(
            "/token",
            data={
                "username": "user1",
                "password": "Password.1",
            },
        )
        assert response.status_code == 200

        # получаем токен доступа
        token_response = response.json()
        access_token = token_response["access_token"]

        # получаем сведения о зарплате сотрудника по его id и токену
        response = await ac.get(
            "/salary/1",  # Используйте реальный ID сотрудника
            headers={"Authorization": f"Bearer {access_token}"}
        )
        print(response)

        # проверяем что данные получены и они присутствуют в ответе
        assert response.status_code == 200
        assert "current_salary" in response.json()
        assert "raise_date" in response.json()
