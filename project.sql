create database bookstore;
use bookstore;

#TODO: user table schema needed!

create table books (
title VARCHAR(256) NOT NULL,
piclink VARCHAR(2083),
format CHAR(9), 
pages INT,
language VARCHAR(32),
authors VARCHAR(256),
publisher VARCHAR(64),
year INT,
ISBN10 CHAR(10) NOT NULL UNIQUE,
ISBN13 CHAR(14) PRIMARY KEY,
CHECK (format = 'paperback' OR format='hardcover'),
available_copy Int
);

#Problem: userid needed as primary key
CREATE TABLE usefulness_rating(
Fid INT AUTO_INCREMENT,#auto generated
score int,
Feedback_toFeedback VARCHAR(256), 
userid VARCHAR(256),
primary key (Fid, userid),
FOREIGN KEY (Feedback_toFeedback, userid) REFERENCES users(login_name, Upassword) ON DELETE CASCADE ON UPDATE CASCADE
);

create table orders (
Odate date not null,
copies INT not null,
Login_name VARCHAR(256) ,
bname VARCHAR(256),
primary key (Odate, Login_name, bname),
foreign key (Login_name) references users(login_name) ON DELETE CASCADE ON UPDATE CASCADE,
foreign key (bname) references books(bname)
);

create table feedback(
Fid INT AUTO_INCREMENT,#auto generated
rank int not null,
Fdate date not null,
Fcomment  VARCHAR(256),
Feedback_giver VARCHAR(256),
bname  VARCHAR(256),
#specific timing
primary key (Fid),
foreign key (Feedback_giver) references users(login_name) ON DELETE CASCADE ON UPDATE CASCADE,
foreign key (bname) references books(bname)
);

#when new record is added to “record transaction”, books table should also be updated
create table record_transaction(
Tid int NOT NULL AUTO_INCREMENT,
Tdate date,
copynum Int,
bname VARCHAR(256),
primary key (Tid),
foreign key (bname) references books(bname)
);

#update the number of copies in table book
create trigger after_transac_update
	after update on record_transaction
	for each row
	update book
	set available_copy = available_copy + record_transaction.copynum
	where book.title = record_transaction.bname;


#bookrecommendation for user who bought A
#select

#bookrecommendation for user who want to buy a book

#storage auto reminding function
#search function(for website)






