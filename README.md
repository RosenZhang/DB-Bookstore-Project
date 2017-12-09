# Bookstore
This is a web application that is implemented using Django 

# Features
These are the following features that are implemented in our bookstore

  * Registration 
  * Ordering
  * User Records
  * Feedback Ratings
  * Usefulness Ratings
  * Browsing 
  * Recommendations
  * Statistics and increasing inventory functions for store manager
  
# Getting startued
## Prerequisites
Packages requirements for the project
  * Python: 2.7,3.6,3.6
  * [MySQL: 5.5,5.6,5.7](https://dev.mysql.com/downloads/installer/)
  * [Django: 1.8,1.9,1.10,1.11](https://docs.djangoproject.com/en/2.0/intro/install/)
  * mysqlclient via
```shell
(virtualenv)$ pip install django-mysql
```

## Running procedure
1. Create DB project, user and grant privilage for user in MySQL
```MySQL
$ source [project location]\bookstoremysqlsetup.sql
```
2. Create schema and corresponding triggers
```MySQL
$ source [project location]\project.sql
```
3. Django load project and create superuser
```shell
# cd to corresponding project folder
# run following command to makemigrations, mostly for authentication purposes
(virtualenv)$ python manage.py makemigrations
(virtualenv)$ python manage.py migrate
# create superuser
(virtualenv)$ python manage.py createsuperuser
```
4. Start service and view bookstore at 127.0.0.1:8000
```shell
# start service
(virtualenv)$ python manage.py runserver
```
5. Remember to use our website to **at least register 4 users** so we can insert more data in next section.
6. Insert data to database!
```MySQL
$ source [project location]\sample.sql
```
7. Now start exploration at our django website 127.0.0.1:8000
# Entity Relationship Diagram
--> INSERT IMAGE HERE

# Relational Schema 
SQL DDL code can be found [here](https://github.com/RosenZhang/DB-Bookstore-Project/blob/schemedesign/project.sql).

# Features
## RESTFUL call

## Django Ajax

# Authors
  * [Zou Yun](https://github.com/pappar1027)
  * [Zhang Ruochen](https://github.com/RosenZhang)
  * [Wu Jinglian](https://github.com/Gilliamwu)
  * [Elaine Cheong](https://github.com/ElaineJ)
  * [He Jiabei](https://github.com/HeJiabei616)

