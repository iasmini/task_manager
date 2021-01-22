# pull official base image
FROM python:3.8.6

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y nano \
    postgresql-client && \
    mkdir /app
RUN echo "alias ll='ls -alF'" >> ~/.bashrc

WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run wait-for-postgres.sh
ENTRYPOINT ["/app/wait-for-postgres.sh"]
