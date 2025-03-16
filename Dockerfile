FROM python:3.10.8-slim

WORKDIR /app

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "core"]