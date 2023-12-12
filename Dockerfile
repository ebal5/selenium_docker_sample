# Base image
FROM python:3.8 AS builder

# Install Google Chrome
RUN apt-get update && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y google-chrome-stable

FROM builder as lib

COPY ./requirements.lock /tmp/requirements.lock
RUN cat /tmp/requirements.lock | sed '/-e/d' > /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

FROM lib as runner

COPY . /sample
WORKDIR /sample

ENTRYPOINT ["python", "src/sample/run.py"]
