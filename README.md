# Simple-API

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
$ python3 -m venv venv
$ . venv/bin/activate
```

#### Or on Windows cmd : 
 ```bash
> py -3 -m venv venv
> venv\Scripts\activate.bat
```

#### Install the requirements :
```bash
$ pip3 install -r requirements.txt
```

####  Run makemigrations and migrate :
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Run the tests :
```bash
python3 manage.py test
```

![image](https://user-images.githubusercontent.com/49264993/169146251-ebef4c57-8e4b-49a1-8717-8716b390de5d.png)


#### Run the development server :
```bash
python3 manage.py runserver
```

