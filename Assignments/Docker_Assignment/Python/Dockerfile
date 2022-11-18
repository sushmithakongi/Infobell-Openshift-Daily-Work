FROM python:3.11

RUN apt install mysql

WORKDIR /usr/app/src

COPY app.py ./

CMD ["python", "./app.py"]