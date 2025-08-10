
# Builder stage
FROM python:3.10-bullseye

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install mysql dependencies
RUN apt-get update && apt-get install -y --no-install-recommends default-libmysqlclient-dev build-essential pkg-config

# Our working directory in the container
WORKDIR /app

# copy and install python dependencies in to the virtual environment
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN groupadd -r django && useradd -r -g django django
RUN chown -R django:django /app

# switch user
USER django

EXPOSE 8000

# commands to run the application in production
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Twender.wsgi:application"]
