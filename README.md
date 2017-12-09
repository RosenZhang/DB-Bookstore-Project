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
  
# Entity Relationship Diagram
![alt text](https://github.com/RosenZhang/DB-Bookstore-Project/blob/master/DB_bookstore.jpg)

# Relational Schema and Sample Data
SQL DDL code can be found [here](https://github.com/RosenZhang/DB-Bookstore-Project/blob/schemedesign/project.sql).
Sample data can be found [here](https://github.com/RosenZhang/DB-Bookstore-Project/blob/schemedesign/sample.sql)

# Getting started
## Prerequisites
Packages requirements for the project
  * Python: 2.7
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
4. Direct to DB-Bookstore-Project/django_test/bookstore and start service running the following command
```shell
# start service
(virtualenv)$ python manage.py runserver
```
5. Remember to use our website to **at least register 5 users** so we can insert more data in next section.
6. Insert data to database!
```MySQL
$ source [project location]\sample.sql
```
7. Now start exploration at our django website 127.0.0.1:8000
# Website Walkthrough
#### Log in as normal customer
1. Log in/ register
    * To register, click the pen button to create a new user and click next to login
    * To login directly, type in you username and password then click student button
2. After log in, you will be directed to your home page including your user information and order history.
3. By click the search book button on the top bar, you will be directed to the search page and you can click any books in your search result for more details
4. In the book details page, you can see detail info about the book and other's feedback on the book.
5. After ordering the book, you'll be directed to the order confirmation page where all the recommendations will be displayed.
#### Log in as store manager
1. Input you superuser account then click manager button to login
2. After login successfully, you'll be directed to home page where transaction history and other statistics will be displayed.
3. By clicking the add new record order, you can input book details to increase the inventory.

# Features
## RESTFUL call

## Django Ajax

# Authors
  * [Zou Yun](https://github.com/pappar1027)
  * [Zhang Ruochen](https://github.com/RosenZhang)
  * [Wu Jinglian](https://github.com/Gilliamwu)
  * [Elaine Cheong](https://github.com/ElaineJ)
  * [He Jiabei](https://github.com/HeJiabei616)

