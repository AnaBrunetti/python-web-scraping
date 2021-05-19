# Overview
APS Unip 5th Semester. Computer Science Course. Web Scraping project with Python Django.

# Requirements

* Python (3.9.1) [Installation](https://www.python.org/downloads/ "Installation") 
* Virtualenv (20.4.3) [Installation](https://pypi.org/project/virtualenv/20.4.3/ "Installation")
* Visual Studio Code (Recomended IDE) [Installation](https://code.visualstudio.com/ "Installation")

# Run project
* Git clone this repository.
* Open ide and project folder (vs used).
* At terminal: <br>
 ```
 $ pip install virtualenv
 $ virtualenv venv -p python
 $ ./venv/scripts/activate
 $ cd web_scrapy
 $ pip install -r requirements.txt
 $ python manage.py collectstatic
 $ python manage.py migrate
 $ python manage.py createsuperuser
 $ python manage.py runserver
 ```
* Access http://127.0.0.1:8000/ or http://localhost:8000/
