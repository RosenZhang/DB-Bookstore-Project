use dbproject;

-- drop table if exists record_transaction;
-- drop table if exists orders;
-- drop table if exists usefulness_rating;
-- drop table if exists feedback;
-- drop table if exists books;
-- 
#basic informat
create table books (
title VARCHAR(256) NOT NULL,
piclink VARCHAR(2083),
format CHAR(9), 
pages INT,
subject varchar(100),
language VARCHAR(32),
authors VARCHAR(256),
publisher VARCHAR(64),
year INT,
ISBN10 CHAR(10) NOT NULL UNIQUE,
ISBN13 CHAR(14) PRIMARY KEY,
CHECK (format = 'paperback' OR format='hardcover'),
available_copy Int
);

create table feedback(
Fid INT AUTO_INCREMENT NOT NULL,#auto generated
rank int not null,
Fdate DATETIME(2),
Fcomment text,
Feedback_giver int(11),
bid CHAR(14),
primary key (Fid),
foreign key (Feedback_giver) references auth_user(id) ON DELETE CASCADE ON UPDATE CASCADE,
foreign key (bid) references books(ISBN13) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE usefulness_rating(
Fid INT,
score int,
userid int(11) NOT NULL,
primary key (Fid, userid),
foreign key (Fid) references feedback(Fid) ON DELETE CASCADE ON UPDATE CASCADE,
foreign key (userid) references auth_user(id) ON DELETE CASCADE ON UPDATE CASCADE
);

#user can order one or more books; for each order, only one book can be ordered, with multiple copies???
create table orders (
Odate DATETIME(2) not null,
copynum INT not null,
userid int(11) ,
bid CHAR(14),
primary key (Odate, userid, bid),
foreign key (userid) references auth_user (id) ON DELETE CASCADE ON UPDATE CASCADE,
foreign key (bid) references books (ISBN13)
);


#when new record is added to “record transaction”, books table should also be updated
#keep arrivals of new books on record for managers to check the history of transactions
create table record_transaction(
Tid int NOT NULL AUTO_INCREMENT,
Tdate DATETIME(2),
copynum Int,
bid CHAR(14),
primary key (Tid),
foreign key (bid) references books(ISBN13)
);

#update the number of copies in table book when there is new transaction
drop trigger if exists after_transac_update;
create trigger after_transac_update
	after insert on record_transaction
	for each row
	update books
	set available_copy = available_copy + new.copynum
	where books.ISBN13 = new.bid;

#update the number of copies in table book when there are new orders from customers
drop trigger if exists not_enought_copy;
DELIMITER //
create trigger not_enought_copy
	after insert on orders
	for each row 
	begin
		if (new.copynum > (select available_copy from books where new.bid = books.ISBN13)) then
			SIGNAL SQLSTATE '45000'
				set message_text = 'Not Available';
		END if;
		END // DELIMITER ;
		
#update the number of copies in table book after receveing an order from customers
drop trigger if exists after_orders;	
create trigger after_orders
	after insert on orders
	for each row
	update books
	set books.available_copy = books.available_copy - new.copynum
	where new.bid = books.ISBN13;






