FROM python:3.10-slim

WORKDIR /app

COPY ./posts/requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY ../proto /app/proto

# COPY . /app/

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
# CMD ["fastapi", "run", "app/main.py", "--port", "80"]