# Simple-API-DynamoDB

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A simple server-less Restful API on Django using the following tech stacks: Python - Django - AWS DynamoDB - S3 \
Ready to deply on AWS Lambda using [Zappa](https://github.com/zappa/Zappa).

# Table of Contents
* [How run the project?](#how-run-the-project)
* [Final Result](#final-result)
* [Frequently Asked Questions](#frequently-asked-questions)

## How run the project?


### Clone the repository :
```bash
$ git clone https://github.com/erfanghorbanee/Simple-API-DynamoDB.git
$ cd Simple-API-DynamoDB
```

### Create a virtualenv and activate it :
 ```bash
$ python -m venv venv
$ . venv/bin/activate
```

### Or on Windows cmd : 
 ```bash
python -m venv venv
venv\Scripts\activate.bat
```

### Install the requirements :
```bash
cd simple_api/

pip install -r requirements.txt
```

### Configure your aws credentials :
```
aws configure
```

now enter your credentials and you're good to go!
```
AWS Access Key ID [None]: MYACCESSKEY
AWS Secret Access Key [None]: MYSECRETKEY
Default region name [None]: MYREGION
Default output format [None]: json
```

###  Run dynamodb migrator :
You can find it at Simple-API/simple_api/dynamodb_migrator.py directory inside the project.\
this is similar to usual makemigrations command that we run all the time, it creates the table we want for this project.\
feel free to change it the way you need.

```bash
python dynamodb_migrator.py
```

Check if your table is created successfully using this command :
```
aws dynamodb list-tables
```

### Config your secret variables!
#### Local:
As you might know, it's not secure to put important variables such as SECRET_KEY directly in the code,\
so instead in the Simple-API/simple_api/ directory create a .env file,\
this will be where we put our variables and fetch it in settings.py using  Python Decouple

example:
```
SECRET_KEY='MYSECRETKEY'
DEBUG=True
```

to learn more, you can check this [article](https://dontrepeatyourself.org/post/how-to-use-python-decouple-with-django/).

#### Production:
In this project, i used zappa to deploy on aws lambda. therefore i have a [zappa_settings.json](https://github.com/erfanghorbanee/Simple-API-DynamoDB/blob/main/simple_api/zappa_settings.json) file and i'm gonna store my environment variables in it!

```json
"environment_variables":{
   "AWS_ACCESS_KEY_ID":"",
   "AWS_SECRET_ACCESS_KEY":"",
   "AWS_STORAGE_BUCKET_NAME":"",
   "AWS_S3_CUSTOM_DOMAIN":"",
   "SECRET_KEY":""
}
```

### Run the development server :
This code is for production, so you have to make a few changes before running it on local server. \
**NOTE: Make sure to configure [settings.py](https://github.com/erfanghorbanee/Simple-API-DynamoDB/blob/main/simple_api/config/settings.py) properly:** \
```python
SECRET_KEY = "SECRET_KEY"
DEBUG = True
STATIC_URL = '/static/'
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"  # Comment this one on local server!
```

**NOTE 2: Put your own aws credentials in [devices/api/views.py](https://github.com/erfanghorbanee/Simple-API-DynamoDB/blob/main/simple_api/devices/api/views.py) to connect to your dynamodb :**
```python
# Get the service resource.
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id="MYACCESSKEY",
    aws_secret_access_key="MYSECRETKEY",
    region_name="MYREGION",
)
table = dynamodb.Table("Devices")
```

```bash
python manage.py runserver
```

### Run the tests :
```bash
python manage.py test
```

## Final Result
We have two api at the moment \
one for creating an instance in dynamo db, \
and another one for getting it.

### Request 1:
```
HTTP POST
URL: http://127.0.0.1:8000/api/v1/devices/
Body (application/json):
```
```json
{
"id": "/devices/id1",
"deviceModel": "/devicemodels/id1",
"name": "Sensor",
"note": "Testing a sensor.",
"serial": "A020000102"
}
```
### Response 1 - Success:
![image](https://user-images.githubusercontent.com/49264993/169469128-8192329f-2073-4b3b-86a5-41bd0f1abc4d.png)

### Response 1 - Failure 1:
If any of the payload fields are missing:

![image](https://user-images.githubusercontent.com/49264993/169469325-c63fca76-3692-4e50-a459-c38cf1fd24e9.png)

<hr>

### Request 2:
```
HTTP GET
URL: http://127.0.0.1:8000/api/v1/devices/id1/
Example: GET https://api123.amazonaws.com/api/devices/id1
```

### Response 2 - Success:
![image](https://user-images.githubusercontent.com/49264993/169470647-37b223cc-5cbf-40b9-a0ce-6465413f2f7e.png)

### Response 2 - Failure 1:
![image](https://user-images.githubusercontent.com/49264993/169471253-7629e908-a21d-4a01-8550-6507911b4642.png)


**NOTE: YOU CAN CHECK YOUR TABLES AND SEE IF THE INSTANCES WERE CREATED SUCCECFULLY:**
```
aws dynamodb scan --table-name Devices
```


## Frequently Asked Questions
### Question 1
Is there any advantage of using integer hash key over string hash key?
### Answer
Serialized numbers are sent to Amazon DynamoDB as String types, which maximizes compatibility across languages and libraries, 
so there shouldn't be any advantage of using an integer hash key over a string hash key.

### Question 2
How can i deploy this on AWS Lambda?
### Answer
Use the following commands in order:
```
$ pip install zappa
$ zappa init
$ zappa deploy
```

for more information, check out this links:
- [Django deploy - Zappa onto AWS Lambda + API Gateway](https://www.youtube.com/watch?v=WaiL4sbaj_o)
- [Django | Configure AWS S3 for Static Storage](https://www.youtube.com/watch?v=-dqpL3aY5e4)
- [Serverless Deployment of a Django Project with AWS Lambda, Zappa, S3 and PostgreSQL](https://www.youtube.com/watch?v=Gf0vpJQZeBI)





