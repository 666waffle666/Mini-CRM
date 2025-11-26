FROM python:3.13-slim

WORKDIR /mini_crm

COPY pyproject.toml poetry.lock ./

RUN pip install poetry
RUN poetry install --no-root

COPY . .

CMD ["poetry", "run", "uvicorn", "mini_crm:app", "--host", "0.0.0.0", "--port", "8000"]