FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN apt-get update
RUN apt-get install software-properties-common || exit 0
RUN apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main'
RUN apt-get update
RUN apt-get install openjdk-8-jdk

ENV JAVAHOME  /usr/lib/jvm/java-8-openjdk-amd64/

RUN pip3 install --no-cache-dir --upgrade pip -r requirements.txt

EXPOSE 9692
CMD [ "python3", "./app.py" ]