FROM python:3.9-alpine

WORKDIR /python-docker
# install necessary packages

ARG CHROMIUM_VERSION
ENV CHROMIUM_VERSION ${CHROMIUM_VERSION}
ENV DOCKER=DOCKER


RUN apk update && \
    apk add --no-cache \
    wait4ports \
    chromium \
    chromium-chromedriver \
    && rm -rf /var/cache/apk/*

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV DISPLAY=:99
EXPOSE 5000
COPY . .
CMD ["python", "-m", "web"]
