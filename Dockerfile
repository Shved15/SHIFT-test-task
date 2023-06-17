FROM python:3.11

WORKDIR /app

ADD . /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

RUN apt-get update && apt-get install -y netcat-openbsd postgresql-client

CMD ["./cmds.sh"]