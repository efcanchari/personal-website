# Docker, Image, Container
FROM python:3.9

ENV DB_USER=root
ENV DB_PASS=root
ENV DB_SERVER=postgre
ENV DB_PORT=5432
ENV DB_NAME=website

ENV FLASK_ENV=development
ENV FLASK_APP=main.py

COPY website /opt/app/website
COPY main.py /opt/app/
COPY requirements.txt /opt/app/
WORKDIR /opt/app

RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","./main.py"]

