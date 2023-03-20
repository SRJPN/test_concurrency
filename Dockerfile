# FROM python:3.8-slim-buster as base

# ARG ENV
# RUN echo $ENV

# RUN mkdir -p /app

# WORKDIR /app

# ADD . /app/

# RUN pip install --upgrade pip
# RUN pip freeze > requirements.txt
# RUN pip install -r requirements.txt

# EXPOSE 8001

# ENV service_name="test-concurrency"

# # CMD ["python", "-m", "django", "manage.py", "runserver", "8001"]
# # CMD ["python", "manage.py", "runserver", "8001"]

# # CMD ["gunicorn", "--bind", ":8001", "--workers", "3", "mysite.wsgi:application"]

# base image  
FROM python:3.8   
# setup environment variable  
ENV DockerHOME=/home/app/webapp

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8001
# start server  
CMD python manage.py runserver 8001