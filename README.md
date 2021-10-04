# Python + Flask + Docker
This is a Python web application using Flask connected to PostgreSQL DB and build in docker
Original on:
https://bitbucket.org/aexperts/personal-website/

## Install pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

- install dependencies
```
pip3 install flask
pip3 install flask_sqlalchemy
pip3 install flask_login
pip3 install pymysql
pip3 install psycopg2
```

- Generate Requirements
```shell
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```

# Docker
- Build image
```
docker build -t website:1.0 .
```

- Tag build image
```
docker tag website:1.0 efcanchari/website:1.0
```

- Push image
```
docker push efcanchari/website:1.0
```