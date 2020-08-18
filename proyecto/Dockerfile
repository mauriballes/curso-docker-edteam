FROM python:3

RUN apt-get update
RUN apt-get install libpq-dev -y
RUN mkdir /app

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

CMD python app.py

EXPOSE 5000