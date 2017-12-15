import json
import datetime
from django.db import connection
from datetime import timedelta
from json import JSONEncoder
import decimal

def remove_quote(inp):
    if(type(inp) == 'str'):
        inp.replace("'","")
        inp.replace('"',"")


######################## basic mysql command
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

from collections import namedtuple
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def my_custom_sql_dict(sql_command_string,command_tuple=None):
    with connection.cursor() as cursor:
        if command_tuple is not None:
            cursor.execute(sql_command_string,command_tuple)
        else:
            cursor.execute(sql_command_string)

        rows = dictfetchall(cursor)
    return rows

def my_custom_sql_tuple(sql_command_string,command_tuple=None):
    with connection.cursor() as cursor:
        if command_tuple is not None:
            cursor.execute(sql_command_string,command_tuple)
        else:
            cursor.execute(sql_command_string)


        rows = cursor.fetchall()
    return rows

######################## json functions
def dict_to_json(input_dict):
    return json.dumps(input_dict)

def json_to_dict(input_json):
    return json.loads(input_json)
########################

def get_book_list():
    cursor = connection.cursor()
    cursor.execute('SELECT title FROM DBproject.books')
    titles = [row[0] for row in cursor.fetchall()]
    return titles

def get_book_list_v2_with_brief_record(title,op1,author,op2,publisher,op3,subject,sorted_by):

    query='select books.*, avg(rank) as avgscore from books left join feedback '\
'on feedback.bid=books.ISBN13 where '\
'(title like %s  {} authors like  %s  {} publisher like  %s {} subject like %s) '\
'group by books.ISBN13'.format(op1,op2,op3)
    if sorted_by=='-':
        query+=';'
    elif sorted_by=='year':
        query+=' order by year desc;'
    elif sorted_by=='average score':
        query+=' order by avgscore desc;'
    titles = []
    details = []
    # books_info = my_custom_sql_dict(query,('%'+title+'%',op1,'%'+author+'%',op2,'%'+publisher+'%',op3,'%'+subject+'%'))
    books_info = my_custom_sql_dict(query,('%'+title+'%','%'+author+'%','%'+publisher+'%','%'+subject+'%'))

    for book_info in books_info:
        book_class = books(**book_info)
        titles.append(book_class.title)
        details.append(book_class._overview_info())
    return titles, details



def get_book_info(input_ISBN13):
    #remove quotation mark
    remove_quote(input_ISBN13)
    book_info =  my_custom_sql_dict("select * from books where ISBN13 = \'{}\'".format(input_ISBN13))[0]
    book_info_save_to_class = books(**book_info)
    return book_info_save_to_class._book_info()

def get_feedback_info(bid, userid):
    remove_quote(bid)
    query = 'select f.Fid, rank, Fdate, Fcomment, usr.username, Feedback_giver,  avg(IFNULL(u.score, 0)) as avgscore'\
' from (feedback f left join usefulness_rating u on f.Fid = u.Fid) join auth_user usr'\
' on f.Feedback_giver = usr.id where f.bid = \'{}\' group by f.Fid order by avgscore desc;'.format(bid)

    feedbacks_info = my_custom_sql_dict(query)
    feedback_result = []
    for each_feedback in feedbacks_info:
        feedback_save_to_class = feedback(**each_feedback)
        feedback_dict=add_able_to_rate_set(feedback_save_to_class._feedback_info(),userid)
        feedback_result.append(feedback_dict)

    return feedback_result


def get_book_list():
    cursor = connection.cursor()
    cursor.execute('SELECT ISBN13 FROM DBproject.books')
    titles = [row[0] for row in cursor.fetchall()]
    return titles

#########################for user catalog page #########################
# todo: need to change input_userid dynamically for all methods in the section
def get_order_history(input_userid):
    remove_quote(input_userid)
    order_info =my_custom_sql_dict("select title, copynum, Odate from books, orders where orders.bid = books.ISBN13 and userid = {}".format(input_userid))
    order_result = []
    for each_order in order_info:
        order_save_to_class = orders(**each_order)
        order_result.append(order_save_to_class._order_info())
    return order_result

def get_user_information(input_userid):
    remove_quote(input_userid)
    user_information_data = my_custom_sql_dict("select username, email, date_joined, last_login from auth_user where id = {}".format(input_userid))[0]
    info_save_to_class = user_information(**user_information_data)
    return info_save_to_class

def get_feedback_history(input_userid):
    remove_quote(input_userid)
    feedback_info = my_custom_sql_dict("select rank, Fdate, Fcomment, title from books,feedback where books.ISBN13 = feedback.bid and Feedback_giver = {}".format(input_userid))
    feedback_history_result = []
    for each_feedback in feedback_info:
        feedback_save_to_class = feedback_history(**each_feedback)
        feedback_history_result.append(feedback_save_to_class._fhistory_info())
    return feedback_history_result

def get_rating_history(input_userid):
    remove_quote(input_userid)
    rating_info = my_custom_sql_dict("select score, Fcomment, username from usefulness_rating, feedback, auth_user where feedback.Fid = usefulness_rating.Fid and feedback.Feedback_giver = auth_user.id and userid = {}".format(input_userid))
    rating_history_result = []

    for rating in rating_info:
        rating_save_to_class = usefulness_rating_history(**rating)
        rating_history_result.append(rating_save_to_class._rating_history_info())
    return rating_history_result
#########################for user catalog page #########################

#########################for book recommendation page#########################
def get_book_recommendation(input_bid):
    remove_quote(input_bid)
    recom_info = my_custom_sql_dict("select ISBN13, title, sum(orders.copynum) AS sales, piclink from orders,books where orders.bid = books.ISBN13 and books.ISBN13 <> %s and userid in ( select userid from orders,books where orders.bid = books.ISBN13 and books.ISBN13 = %s) group by bid order by sales desc",(input_bid,input_bid))

    recom_result = []

    for book in recom_info:
        recom_save_to_class = recommendations(**book)
        recom_result.append(recom_save_to_class.recom_info())
    return recom_result
#########################for book recommendation page#########################

def get_feedback_info_with_limit(bid, userid,limit):
    remove_quote(bid)
    remove_quote(limit)
    limit=int(limit)
    query = 'select f.Fid, rank, Fdate, Fcomment, usr.username, Feedback_giver,  avg(IFNULL(u.score, 0)) as avgscore'\
' from (feedback f left join usefulness_rating u on f.Fid = u.Fid) join auth_user usr'\
' on f.Feedback_giver = usr.id where f.bid = %s group by f.Fid order by avgscore desc limit %s;'

    feedbacks_info = my_custom_sql_dict(query,(bid,limit))
    feedback_result = []
    for each_feedback in feedbacks_info:
        feedback_save_to_class = feedback(**each_feedback)
        feedback_dict=add_able_to_rate_set(feedback_save_to_class._feedback_info(),userid)
        feedback_result.append(feedback_dict)

    return feedback_result

def add_able_to_rate_set(feedbackdict,userid):
#user cannot rate their own comment
    if userid==feedbackdict['Feedback_giver']:
        ableToRate=False
#user cannot rate comment that has been rated by them
    else:
        fid=feedbackdict['Fid']
        ableToRate= not check_user_rated_feedback(userid,fid)
    feedbackdict['ableToRate']=ableToRate
    return feedbackdict

def check_user_rated_feedback(userid,fid):
    query='select * from usefulness_rating where fid={} and userid={}'.format(fid,userid)
    result=my_custom_sql_tuple(query)
    if len(result)==0:
        return False#user has not rated
    else:
        return True#user has rated

def return_user_usefulness_rate(fid, userid):
    #feedbacks_info = my_custom_sql_dict()
    # TODO: return all the usefulness rate user has done about the book. If there's no record it returns null
    query = 'select score from usefulness_rating where userid = {} and Fid = {};'.format(userid, fid)
    result = my_custom_sql_tuple(query)
    if result == ():
        return None
    else:
        return result[0][0]

def save_user_usefulness_rating(fid, score, userid ):
    cursor = connection.cursor()
    cursor.execute('insert into usefulness_rating values ({}, {}, {});'.format(fid, score, userid))

def save_user_order(userid, copynum, ISBN13):
    cursor = connection.cursor()
    query = 'insert into orders values (current_timestamp(), %s, %s, %s);'

    cursor.execute(query,(copynum, userid, ISBN13))


def save_user_feedback(userid,ISBN13,rank,Fcomment):
    cursor=connection.cursor()
    query='insert into feedback values (null,%s,current_timestamp(), %s, %s, %s);'

    cursor.execute(query,(rank, Fcomment, userid, ISBN13))

def check_user_has_posted_feedback(userid,bid):
    cursor=connection.cursor()

    query='select distinct Feedback_giver from feedback where bid=\'{}\';'.format(bid)
    cursor.execute(query)
    users = [row[0] for row in cursor.fetchall()]
    return (userid in users)

def check_book_exists(bid):
    book_list=get_book_list()
    if bid in book_list:
        return True
    else:
        return False


def add_new_book_and_transaction(title,piclink,format,pages,subject,language,authors,publisher,year,isbn10,bid,available_copy,copynum):
    cursor=connection.cursor()
    query='insert into books values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.execute(query,(title,piclink,format,pages,subject,language,authors,publisher,year,isbn10,bid,available_copy))

    query='insert into record_transaction values (null,current_timestamp(),%s,%s);'
    cursor.execute(query,(copynum, bid))




def save_transaction(copynum, bid):
    cursor=connection.cursor()
    query='insert into record_transaction values (null,current_timestamp(),%s,%s);'
    cursor.execute(query,(copynum, bid))



def get_record_transaction_info():
    record_transaction_info = my_custom_sql_dict("SELECT Tid, Tdate, copynum, title, bid, available_copy FROM record_transaction, books WHERE bid = books.ISBN13")
    record_transaction_result = []

    for each_record_transaction in record_transaction_info:
        record_transaction_save_to_class = record_transaction(**each_record_transaction)
        record_transaction_result.append(record_transaction_save_to_class._record_transaction_info())

    return record_transaction_result

def get_order_author_info(limit=None):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.datetime.now().replace(microsecond=0).strftime(format)
    previous =(datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(-30)).strftime(format)
    if limit is not None and limit !='':
        limit=int(limit)
        order_author_info = my_custom_sql_dict("select books.authors,sum(orders.copynum) AS copynum from books, orders where books.ISBN13 = orders.bid and orders.Odate BETWEEN '%s' AND '%s' group by authors order by copynum DESC Limit %d"%(previous,now,limit))
    else:
        order_author_info = my_custom_sql_dict("select books.authors,sum(orders.copynum) AS copynum from books, orders where books.ISBN13 = orders.bid and orders.Odate BETWEEN '%s' AND '%s' group by authors order by copynum DESC"%(previous,now))

    order_author_result = []

    for each_order_author in order_author_info:
        order_author_save_to_class = order_author(**each_order_author)
        order_author_result.append(order_author_save_to_class._order_author_info())

    return order_author_result

def get_order_title_info(limit=None):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.datetime.now().replace(microsecond=0).strftime(format)
    previous =(datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(-30)).strftime(format)

    if limit is not None and limit !='':
        limit=int(limit)
        order_title_info = my_custom_sql_dict("select books.title,sum(orders.copynum) AS copynum from books, orders where books.ISBN13 = orders.bid and orders.Odate BETWEEN '%s' AND '%s' group by title order by copynum DESC Limit %d"%(previous,now,limit))

    else:
        order_title_info = my_custom_sql_dict("select books.title,sum(orders.copynum) AS copynum from books, orders where books.ISBN13 = orders.bid and orders.Odate BETWEEN '%s' AND '%s' group by title order by copynum DESC"%(previous,now))
    order_title_result = []

    for each_order_title in order_title_info:
        order_title_save_to_class = order_title(**each_order_title)
        order_title_result.append(order_title_save_to_class._order_title_info())

    return order_title_result

def get_order_publisher_info(limit=None):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.datetime.now().replace(microsecond=0).strftime(format)
    previous =(datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(-30)).strftime(format)

    if limit is not None and limit !='':
        limit=int(limit)
        order_publisher_info = my_custom_sql_dict("select books.publisher,sum(orders.copynum) AS copynum from books, orders where books.ISBN13 = orders.bid and orders.Odate BETWEEN '%s' AND '%s' group by publisher order by copynum DESC Limit %d"%(previous,now,limit))

    else:
        order_publisher_info = my_custom_sql_dict("select books.publisher,sum(orders.copynum) AS copynum from books, orders where books.ISBN13 = orders.bid and orders.Odate BETWEEN '%s' AND '%s' group by publisher order by copynum DESC"%(previous,now))
    order_publisher_result = []


    for each_order_publisher in order_publisher_info:
        order_publisher_save_to_class = order_publisher(**each_order_publisher)
        order_publisher_result.append(order_publisher_save_to_class._order_publisher_info())

    return order_publisher_result
  

class books:
    def __init__(self, title="NA", piclink="NA", format="NA",
                 pages="NA", subject="NA", language="NA", authors="NA", publisher="NA",
                 year="NA", ISBN10="NA", ISBN13="NA", available_copy="NA",avgscore="NA" ):
        self.title = title
        self.piclink = piclink
        self.format = format
        self.pages = pages
        self.subject = subject
        self.language = language
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.ISBN10 = ISBN10
        self.ISBN13 = ISBN13
        self.available_copy = available_copy
        self.avgscore=avgscore
        self.overview = {}
        self.info = {}
        self.recom_info = {}

    def _overview_info(self):
        if not self.overview:
            self.overview = {'title':self.title,
                                           'ISBN13':self.ISBN13,
                                           'authors':self.authors,
                                           'publisher':self.publisher,
                                           'subject':self.subject}
        return self.overview

    def _book_info(self):
        if not self.info:
            self.info = {'piclink': self.piclink, 'title':self.title, 'format':self.format,
                                 'ISBN13':self.ISBN13, 'ISBN10':self.ISBN10,"authors":self.authors,'pages':self.pages,
                                 'language':self.language,'publisher':self.publisher, 'year':self.year, 'available_copy':self.available_copy,'subject':self.subject}
        return self.info

    def book_info_json(self):
        if not self.info:
            self._book_info()
        return  dict_to_json(self.info)

    def book_overview_json(self):
        if not self.overview:
            self._overview_info()
        return dict_to_json(self.overview)

    def get_key(self):
        return "ISBN13"+self.ISBN13

class feedback:
    def __init__(self, Fid, rank, Fdate, Fcomment, username, Feedback_giver, avgscore=0):
        self.Fid = Fid#
        self.rank = rank#
        self.username = username
        self.Fdate=Fdate
        self.Fcomment = Fcomment#
        self.Feedback_giver = Feedback_giver#
        self.avgscore = avgscore#
    def _feedback_info(self):
        self.result = {}
        self.result = {'Fid':self.Fid, 'rank':self.rank, 'Fdate':self.Fdate, 'username':self.username, 'Feedback_giver': self.Feedback_giver, "Fcomment":self.Fcomment, "avgscore":self.avgscore}
        return self.result

    def get_key(self):
        return "Fid"+self.Fid

class orders:
    def __init__(self, title, copynum, Odate):
        self.Odate = Odate
        self.copynum = copynum
        self.title = title

    def _order_info(self):
        self.result = {}
        format = '%Y-%m-%d %H:%M:%S'
        self.Odate = self.Odate.strftime(format)
        self.result = {'title':self.title,'copynum':self.copynum,'Odate':self.Odate}
        return self.result

class record_transaction:
    def __init__(self, Tid, Tdate, copynum, title, available_copy, bid):
        self.Tid = Tid
        self.Tdate = Tdate
        self.copynum = copynum
        self.title = title
        self.bid = bid
        self.available_copy = available_copy
        self.info = {}

    def _record_transaction_info(self):
        if not self.info:
            self.info = {'Tid': self.Tid, 'Tdate': self.Tdate, 'copynum': self.copynum,
                         'title': self.title, 'bid': self.bid, 'available_copy': self.available_copy}
        return self.info

class user_information:
    def __init__(self, username, email, date_joined, last_login):
        self.username= username
        self.email = email
        self.date_joined = date_joined
        self.last_login = last_login

    def _user_info(self):
        self.result = {}
        format = '%Y-%m-%d %H:%M:%S'
        self.date_joined = self.date_joined.strftime(format)
        self.last_login = self.last_login.strftime(format)
        self.result = {'username':self.username,'email':self.email,'date_joined':self.date_joined,'last_login':self.last_login}
        return self.result

class feedback_history:
    def __init__(self, title, Fcomment, rank, Fdate):
        self.rank = rank
        self.Fdate = Fdate
        self.Fcomment = Fcomment
        self.title = title

    def _fhistory_info(self):
        self.result = {}
        format = '%Y-%m-%d %H:%M:%S'
        # self.Fdate = self.Fdate.strftime(format)
        self.result = {'title':self.title,'rank':self.rank,'Fcomment':self.Fcomment, 'Fdate':self.Fdate}
        return self.result

class usefulness_rating_history:
    def __init__(self, username, Fcomment, score):
        self.username = username
        self.Fcomment = Fcomment
        self.score = score

    def _rating_history_info(self):
        self.result = {}
        self.result = {'feedback_giver':self.username,'Fcomment':self.Fcomment,'score':self.score}
        return self.result

class recommendations:
    def __init__(self, ISBN13, title,sales, piclink):
        self.ISBN13 = ISBN13
        self.sales = sales
        self.title = title
        self.piclink = piclink

    def recom_info(self):
        self.result={}
        self.result = {'ISBN13':self.ISBN13,'title':self.title,'sales':self.sales,'piclink':self.piclink}
        return self.result

class order_author:
    def __init__(self, authors, copynum):
        #self.Odate = Odate
        self.authors = authors
        self.copynum = copynum

    def _order_author_info(self):
        self.result = {}
        # format = '%Y-%m-%d %H:%M:%S'
        # self.Odate = self.Odate.strftime(format)
        self.result = {'authors':self.authors,'copynum':self.copynum }
        return self.result

class order_title:
    def __init__(self, title, copynum):
        #self.Odate = Odate
        self.title = title
        self.copynum = copynum

    def _order_title_info(self):
        self.result = {}
        # format = '%Y-%m-%d %H:%M:%S'
        # self.Odate = self.Odate.strftime(format)
        self.result = {'title':self.title,'copynum':self.copynum }
        return self.result

class order_publisher:
    def __init__(self, publisher, copynum):
        #self.Odate = Odate
        self.publisher = publisher
        self.copynum = copynum

    def _order_publisher_info(self):
        self.result = {}
        # format = '%Y-%m-%d %H:%M:%S'
        # self.Odate = self.Odate.strftime(format)
        self.result = {'publisher':self.publisher,'copynum':self.copynum }
        return self.result


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)