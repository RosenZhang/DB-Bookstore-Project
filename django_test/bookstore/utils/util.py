import json
import datetime
from django.db import connection

from . import fetched_class


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

def my_custom_sql_dict(sql_command_string):
    with connection.cursor() as cursor:
        cursor.execute(sql_command_string)
        rows = dictfetchall(cursor)
        print("==========================", rows,"===================")
    return rows

def my_custom_sql_tuple(sql_command_string):
    with connection.cursor() as cursor:
        cursor.execute(sql_command_string)
        rows = cursor.fetchall()
        print("==========================", rows,"===================")
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
    #db.close()
    return titles

def get_book_info(input_ISBN13):
    book_info =  my_custom_sql_dict("select * from books where ISBN13 = '%s'" %(input_ISBN13))[0]
    book_info_save_to_class = books(**book_info)
    fetched_class.register_class(book_info_save_to_class)
    print ("\n\n =============dictionary info================", book_info_save_to_class._book_info())
    return book_info_save_to_class._book_info()


def get_feedback_info(bid, userid):
    query = 'select distinct f.*, u.score from feedback f left join (select * from usefulness_rating where userid = {}) ' \
            'u on feedback_giver != u.userid and f.fid = u.fid where f.bid = \'{}\';'.format(userid, bid)

    print("query===========================--------{}------\n\n".format(query))
    feedbacks_info = my_custom_sql_dict(query)
    print("query=====================feedback_info======--------{}------\n\n".format(feedbacks_info))
    feedback_result = []
    for each_feedback in feedbacks_info:
        feedback_save_to_class = feedback(**each_feedback)
        feedback_result.append(feedback_save_to_class._feedback_info())

    print("feedback result===========================--------------", feedback_result)
    return feedback_result


def get_book_list():
    cursor = connection.cursor()
    cursor.execute('SELECT title FROM DBproject.books')
    titles = [row[0] for row in cursor.fetchall()]
    return titles

def get_order_history(input_userid = 1):
    order_info =my_custom_sql_dict("select title, copynum, Odate from books, orders where orders.bid = books.ISBN13 and userid = '%s'" %(input_userid))
    print order_info [0]
    order_result = []
    for each_order in order_info:
        order_save_to_class = orders(**each_order)
        order_result.append(order_save_to_class._order_info())
    return order_result


def return_user_usefulness_rate(fid, userid):
    #feedbacks_info = my_custom_sql_dict()
    # TODO: return all the usefulness rate user has done aboutu the book. If there's no record it returns null
    query = 'select score from usefulness_rating where userid = {} and Fid = {};'.format(userid, fid)
    result = my_custom_sql_tuple(query)
    if result == ():
        return None
    else:
        print("______+++++++++++++++++++++++++++++++++_______________ result of usefulness rate", result[0][0], '\n\n')
        return result[0][0]

def save_user_usefulness_rating(fid, score, userid ):
    cursor = connection.cursor()
    cursor.execute('insert into usefulness_rating values ({}, {}, {});'.format(fid, score, userid))

def save_user_order(userid, copynum, ISBN13):
    cursor = connection.cursor()
    query = 'insert into orders values (current_timestamp(), {}, {}, {});'.format(userid, copynum, ISBN13)
    print('========================================== query: ', query)
    cursor.execute(query)


class books:
    def __init__(self, title="NA", piclink="NA", format="NA",
                 pages="NA", subject="NA", language="NA", authors="NA", publisher="NA",
                 year="NA", ISBN10="NA", ISBN13="NA", available_copy="NA" ):
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
        self.overview = {}
        self.info = {}
        self.recom_info = {}

    def _overview_info(self):
        if not self.overview:
            self.overview['bookoverview']={'piclink':self.piclink,'title':self.title,'authors':self.authors,
                                           'publisher':self.publisher}
        return self.overview

    def _book_info(self):
        if not self.info:
            self.info = {'piclink': self.piclink, 'title':self.title, 'format':self.format,
                                 'ISBN13':self.ISBN13,"authors":self.authors,'pages':self.pages,
                                 'language':self.language,'publisher':self.publisher, 'year':self.year}
        return self.info

    def _recommentdation_info(self):
        if not self.recom_info:
            self.recom_info["recommendations"]={'title','piclink'}

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
    def __init__(self, Fid, rank, Fdate, Fcomment, Feedback_giver, bid, score=0):
        self.Fid = Fid
        self.rank = rank
        self.Fdate = Fdate
        self.Fcomment = Fcomment
        self.Feedback_giver = Feedback_giver
        self.bid = bid
        self.score = score
    def _feedback_info(self):
        self.result = {}
        self.result = {'Fid':self.Fid, 'Feedback_giver': self.Feedback_giver, "Fcomment":self.Fcomment, "Score":self.score}
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
    def __init__(self, Tid, Tdate, copynum, bid):
        self.Tid = Tid
        self.Tdate = Tdate
        self.copynum = copynum
        self.bid = bid