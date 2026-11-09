
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --prefix=/install
RUN useradd -m appuser


FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .
RUN useradd -m appuser
USER appuser
CMD ["python", "app.py"]