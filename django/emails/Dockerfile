# Use a newer Python base image with Debian Buster
FROM python:3.6.15-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

# Install PostgreSQL client and libraries
RUN apt-get update \
    && apt-get install -y postgresql-client libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy your application code
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt
