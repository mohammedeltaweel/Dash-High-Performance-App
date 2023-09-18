# Use the official Python base image with Alpine Linux
FROM python:3.10.9-slim as build  

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app

# start the server
CMD ["gunicorn", "layout:server", "-b", "0.0.0.0:8089", "-w", "4"]