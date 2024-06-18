FROM python:3.11.5-bullseye 

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip 

COPY . /app/

RUN mkdir -p /app/staticfiles/

RUN pip install -r requirements.txt  

EXPOSE 8000

CMD ["uvicorn", "mysaas.asgi:application", "--host", "0.0.0.0"]
