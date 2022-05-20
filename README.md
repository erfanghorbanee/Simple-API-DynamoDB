# Simple-API

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

 A simple Restful API on Django using the following tech stack: Python - Django - AWS DynamoDB


## How run the project?


#### Clone the repository :
```bash
$ git clone https://github.com/erfanghorbanee/Simple-API.git
$ cd Simple-API
```

#### Create a virtualenv and activate it :
 ```bash
$ python -m venv venv
$ . venv/bin/activate
```

#### Or on Windows cmd : 
 ```bash
python -m venv venv
venv\Scripts\activate.bat
```

#### Install the requirements :
```bash
cd simple_api/

pip install -r requirements.txt
```

#### Configure your aws credentials :
```
aws configure
```

now enter your credentials and you're good to go!
```
AWS Access Key ID [None]: MYACCESSKEY
AWS Secret Access Key [None]: MYSECRETKEY
Default region name [None]: MYREGION
```

####  Run dynamodb migrator :
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

#### Config your secret variables!
As you might know, it's not secure put important variables such as SECRET_KEY directly in the code,\
so instead in the Simple-API/simple_api/ directory create a .env file,\
this will be where we put our variables and fetch it in settings.py using  Python Decouple

```
SECRET_KEY='MYSECRETKEY'
DEBUG=True
```

to learn more, you can check this [article](https://dontrepeatyourself.org/post/how-to-use-python-decouple-with-django/).

#### Run the tests :
```bash
python manage.py test
```

#### Run the development server :
```bash
python manage.py runserver
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

for more information, check out this links: \
[Zappa repository](https://github.com/zappa/Zappa) \
[Django deploy - Zappa onto AWS Lambda + API Gateway](https://www.youtube.com/watch?v=WaiL4sbaj_o)





