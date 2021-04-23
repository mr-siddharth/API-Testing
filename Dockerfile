FROM python:3.9.4

RUN pip install pytest
RUN pip install pytest-html
RUN pip install requests
RUN pip install pytest-xdist
RUN pip install mysql-connector-python
RUN pip install requests-oauthlib

ENV ENV=docker

RUN mkdir -p /home/api-testing
COPY . /home/api-testing
