#3
#print full record of a userX

#1) his/her account information
select * from auth_user
where username = userX;

# his/her full history of orders (book name, number of copies, date etc.)
select title, copynum, Odate from orders,books
where userid = 1
and books.ISBN13 = orders.bid;

# his/her full history of feedbacks from user 1
select Fid, rank, Fdate, Fcomment, title from books,feedback
where Feedback_giver = 1
and books.ISBN13 = feedback.bid;

# the list of all the feedbacks he/she ranked with respect to usefulness
select score, Fcomment, username from usefulness_rating, feedback, auth_user
where userid = 1
and feedback.Fid = usefulness_rating.Fid
and feedback.Feedback_giver = auth_user.id;


#4  insert new books for store manager
insert into books values (); #(<title>,<piclink>,<format>,<pages>,<subject>,<language>,<authors>,<publisher>, <year>,<ISBN10>,<ISBN13>,<available_copy>)

#5  The store manager increases the number of copies in inventory.
insert into record_transaction values ();#(<copynum>,<bid>)

#7 user view all feedback but can only rate others (is it part in django?)
select * from feedback;


#8 asking conjunctive queries on the authors, and/or publisher, and/or title, and/or subject
### order by year in descending order
select * from books
-- where authors = input_author_optional
-- and publisher = input_publisher_optional
-- and title  = input_title_optinal
-- and subject = input_subject_optional
order by year desc;

#### order by avg feedback
select books.*, avg(rank) from books,feedback
where books.ISBN13 = feedback.bid
-- and authors = input_author_optional
-- and publisher = input_publisher_optional
-- and title  = input_title_optinal
-- and subject = input_subject_optional
group by feedback.bid
order by avg(rank) desc;

#9 For a given book, a user could ask for the top n most useful feedbacks. 
#The usefulness of a feedback is its average usefulness score.

select auth_user.username, Fcomment, avg(usefulness_rating.score) as avgscore
from feedback, usefulness_rating, books, auth_user
where feedback.Fid = usefulness_rating.Fid
and books.ISBN13 = feedback.bid
and books.title = 'The Great Gatsby'
and feedback.Feedback_giver = auth_user.id
group by usefulness_rating.Fid
order by avg(score) desc
limit 3;

#10 Book recommendation: including the user his own ordering history

select title, sum(orders.copynum) AS sales from orders,books
where orders.bid = books.ISBN13
and books.ISBN13 <> 1
and userid in (
select userid
from orders,books
where orders.bid = books.ISBN13
and books.ISBN13 = 1)
group by bid
order by sales desc;

#11
#the list of the m most popular books (in terms of copies sold in this month)
select books.authors,sum(orders.copynum) from books, orders
where books.ISBN13 = orders.bid and orders.Odate BETWEEN '2017-10-20 00:00:00' AND '2017-11-30  23:59:59'
group by authors
order by sum(orders.copynum) DESC
limit 2;

#the list of m most popular authors
select books.title,sum(orders.copynum) from books, orders
where books.ISBN13 = orders.bid and orders.Odate BETWEEN '2017-10-20 00:00:00' AND '2017-11-30  23:59:59'
group by title
order by sum(orders.copynum) DESC
limit 2;

#the list of m most popular publishers
select books.publisher,sum(orders.copynum) from books, orders
where books.ISBN13 = orders.bid and orders.Odate BETWEEN '2017-10-20 00:00:00' AND '2017-11-30  23:59:59'
group by publisher
order by sum(orders.copynum) DESC
limit 2;

#返回feedback score
select score
from usefulness_rating
where userid = someuserid
and Fid = someFid;
