#4  insert new books
insert into books values (); #(<title>,<piclink>,<format>,<pages>,<subject>,<language>,<authors>,<publisher>, <year>,<ISBN10>,<ISBN13>,<available_copy>)

#5
insert into record_transaction values ();#(<copynum>,<bid>)

#7 user view all feedback but can only rate others (is it part in django?)
select * from feedback;


#8
### order by year
select * from books
where authors = input_author_optional
and publisher = input_publisher_optional
and title  = input_title_optinal
and subject = input_subject_optional
order by year desc;

#### order by avg feedback
select books.*, avg(score) from books,feedback,usefulness_rating
where books.ISBN13 = feedback.bid and feedback.Fid = usefulness_rating.Fid
and authors = input_author_optional
and publisher = input_publisher_optional
and title  = input_title_optinal
and subject = input_subject_optional
group by feedback.bid
order by avd(score) desc;

