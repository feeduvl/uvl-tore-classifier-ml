FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y wget
RUN wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | apt-key add -
RUN add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
RUN apt-get update && apt-get install -y adoptopenjdk-8-hotspot

ENV JAVAHOME  /usr/lib/jvm/java-8-openjdk-amd64/

RUN pip3 install --no-cache-dir --upgrade pip -r requirements.txt

EXPOSE 9692
CMD [ "python3", "./app.py" ]