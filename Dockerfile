FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY rxconfig.py .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install -e .

# Create necessary symlinks
RUN mkdir -p /app/frontend
RUN ln -s /app/frontend/portubot /app/portubot 2>/dev/null || true

EXPOSE 3000
CMD ["reflex", "run", "--frontend-port", "3000", "--backend-host", "0.0.0.0"]