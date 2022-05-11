FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN apt-get update && \
     apt-get install -y openjdk-8-jdk-headless && \
    rm -rf /var/lib/apt/lists/*
ENV JAVAHOME  /usr/lib/jvm/java-8-openjdk-amd64/

RUN pip3 install --no-cache-dir --upgrade pip -r requirements.txt

EXPOSE 9692
CMD [ "python3", "./app.py" ]