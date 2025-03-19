FROM python:3.12-slim as builder

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir --user poetry poetry-plugin-export

RUN python3 -m poetry export --without-hashes --format=requirements.txt --output=requirements.txt

FROM python:3.12-slim

COPY --from=builder requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD python manage.py runserver 80

EXPOSE 80