FROM python:3.8.5-slim

LABEL MAINTAINER="Marcelo Lino <mdslino@gmail.com>"

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.4

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY . /app

EXPOSE 80

CMD ["gunicorn", "src.main:app", "--access-logfile=-", "--error-logfile=-", "--log-level=info", "-w 4", "-k uvicorn.workers.UvicornWorker", "-b 0.0.0.0:80"]