# Bookstore
This is a web application that is implemented using Django 

# Project Requirements
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
  * Python: 3.5
  * [MySQL: 5.5,5.6,5.7](https://dev.mysql.com/downloads/installer/)
  * [Django: 1.8,1.9,1.10,1.11](https://docs.djangoproject.com/en/2.0/intro/install/)
  * mysqlclient by following command
```shell
(virtualenv)$ pip install django-mysql
```

## Running procedure
1. Create DB project, user and grant privilage for user in MySQL
```MySQL
$ source [project location]/bookstoremysqlsetup.sql
```
2. Create schema and corresponding triggers
```MySQL
$ source [project location]/project.sql
```
3. Django load project and create superuser
Superuser is the store manager, and you can only use superuser to explore our store manager sites after logging in.
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
$ source [project location]/sample.sql
```
7. Now start exploration at our django website 127.0.0.1:8000
# Website Walkthrough
#### Log in as normal customer
1. Log in/ register
    * To register, click the pen button to create a new user and click next to login
    * To login directly, type in you username and password then click student button
![alt text](https://github.com/RosenZhang/DB-Bookstore-Project/blob/master/Login.png)
2. After log in, you will be directed to your home page including your user information and order history.
![alt text](https://github.com/RosenZhang/DB-Bookstore-Project/blob/master/User_Profile.png)
3. By click the search book button on the top bar, you will be directed to the search page and you can click any books in your search result for more details
4. In the book details page, you can see detail info about the book and other's feedback on the book.
5. After ordering the book, you'll be directed to the order confirmation page where all the recommendations will be displayed.
![alt text](https://github.com/RosenZhang/DB-Bookstore-Project/blob/master/RecommendationPage.png)
#### Log in as store manager
1. Input you superuser account then click manager button to login
![alt text](https://github.com/RosenZhang/DB-Bookstore-Project/blob/master/Storemanager.png)
2. After login successfully, you'll be directed to home page where transaction history and other statistics will be displayed.
3. By clicking the add new record order, you can input book details to increase the inventory.

# Features
#### Double checking of commenting data
When we are adding data via website, our front end will have check of all the conditions (number of available copies, data format etc), and in Database, schema and trigger design also makes sure no bad datas are inserted, like any order of unexisting books. Our double protection makes sure the correctness and safety of the whole bookstore system.

#### MySQL collection utils
All MySQL handling are put under project/utils/util file, for clear management of the code in Django.

#### RESTFUL call
For passing of information within the program, like the passing ISBN13 of book between genearl book page and book details page, we basically use RESTful call. We will pass parameters via URL conf and use Restful API, by simply registering viewsets with a router class. The RESTful call make whole structure more seralized and easier for debugging.

#### Django Ajax
Ajax request is used in web application as it makes whole application faster and more dynamic when HTML pass data to script. AJAX also helps to avoid inline scripts. AJAX works together with JQuery, make part of page reloadable and thus reduce the number of pages loads.
Examples of Ajax could be seen at almost all our html pages that POST data to corresponding views.py.

#### Code recycling
To make the whole project more efficient, we implement idea of code recycling. The template folder only contains base.html that from which all other websites inherit from. Base html has HOME, SEARCH BOOK, LOGOUT that leads to corresponding website, so user can direct use any of these function on every website (home page/book page/ order confirmation page/ store manager page).

#### Recommendation
Book recommendation:when a user orders book A, system will recommend books based on ordering records including the user his own ordering history. Suggested books are arranged in S-type((2n+1)th row, from left to right; (2n)th row, from right to left) on decreasing sales count.

#### Usage of git
Our team use git as our main platform so even every team member works on different features, code is still regulated under one big project. Everyone has a branch and we can view eacn one's update and commitment clearly.

# Authors
  * [Zou Yun 1001831](https://github.com/pappar1027)
  * [Zhang Ruochen 1001433](https://github.com/RosenZhang)
  * [Wu Jinglian 1001428](https://github.com/Gilliamwu)
  * [Elaine Cheong 1001721](https://github.com/ElaineJ)
  * [He Jiabei 1001435](https://github.com/HeJiabei616)

# Acknowledgments
We appreciate Professor Dorien Herremans for teaching us database knowledge and Jon Wong for introducing Django and agile in SUTD 50.008 couse from September to December 2017.
