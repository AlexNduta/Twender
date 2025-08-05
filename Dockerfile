FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Our working directory in the container
WORKDIR /app

# install mysql dependencies
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential pkg-config

# copy and install python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project code into the container
COPY . .

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
