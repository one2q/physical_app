FROM python:3.10-slim


WORKDIR /app
COPY requirements.txt .
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt
COPY . .


#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
