FROM ubuntu:22.04

RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libmagic-dev
RUN pip install loguru
RUN pip install paho-mqtt
RUN pip install python-magic
RUN pip install behave-html-formatter

RUN mkdir /panduza-py
ENV PYTHONPATH="/panduza-py"

WORKDIR /panduza-py
