# build image from official 
FROM python:3.9.6-alpine

#Copy file to root directory
COPY requirements.txt .
COPY main.py .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip3 install -r requirements.txt --timeout 100

#1st command to be executed, we use gunicorn because flask can not do logging by itself
CMD ["gunicorn","-w 2","main:app","-b 0.0.0.0:5000"] 

