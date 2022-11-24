FROM python:3.5

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py", "--host=0.0.0.0"]

EXPOSE 8000