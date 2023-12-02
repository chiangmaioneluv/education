FROM python:3.9.18-alpine3.18

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY templates templates

EXPOSE 5000

CMD [ "python", "main.py" ]
