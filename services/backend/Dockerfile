FROM python:3.9-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.
ENV FRONTEND_URL=https://prueba-toteat-front.herokuapp.com

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# for migrations
COPY migrations .
COPY pyproject.toml .

COPY . /app

CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT}"]
