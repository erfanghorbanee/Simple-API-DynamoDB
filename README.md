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

#### Create a virtualenv and activate it:
 ```bash
$ python -m venv venv
$ . venv/bin/activate
```

#### Or on Windows cmd : 
 ```bash
py -3 -m venv venv
venv\Scripts\activate.bat
```

#### Install the requirements :
```bash
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

#### Run the tests :
```bash
python3 manage.py test
```

#### Run the development server :
```bash
python manage.py runserver
```

## Frequently Asked Questions
### Question 1
Is there any advantage of using integer hash key over string hash key?
### Answer
Serialized numbers are sent to Amazon DynamoDB as String types, which maximizes compatibility across languages and libraries, 
so there shouldn't be any advantage of using an integer hash key over a string hash key.



