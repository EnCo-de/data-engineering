FROM python:3.12.5-slim
RUN pip install psycopg2-binary
COPY ./app /app
ENTRYPOINT  ["python3", "app/stream.py" ]