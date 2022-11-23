FROM python:3.9.13

RUN pip install mysql-connector-python

WORKDIR /usr/app/src

COPY app.py ./

CMD [ "python", "./app.py" ]