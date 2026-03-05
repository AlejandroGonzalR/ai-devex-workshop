FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir virtualenv

COPY . .

RUN virtualenv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir -e .

CMD ["scaffold", "--help"]
