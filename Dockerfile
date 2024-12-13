FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY poetry.lock pyproject.toml /app/
COPY ./backend /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install
