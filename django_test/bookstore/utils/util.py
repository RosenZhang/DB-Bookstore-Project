import json

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

def get_book_info(input_ISBN13):
    book_info =  my_custom_sql_dict("select * from books where ISBN13 = '%s'" %(input_ISBN13))[0]
    book_info_save_to_class = books(**book_info)
    fetched_class.register_class(book_info_save_to_class)
    print ("\n\n =============dictionary info================", book_info_save_to_class._book_info())
    return book_info_save_to_class._book_info()


def get_feedback_info(Fid=1):
    feedbacks_info = my_custom_sql_dict("select * from feedback where Fid = '%s'" %(1))
    # TODO: handle multiple feedbacks. currently only one:
    feedback_result = []
    for each_feedback in feedbacks_info:
        feedback_save_to_class = feedback(**each_feedback)
        feedback_result.append(feedback_save_to_class._feedback_info())
    return feedback_result

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
    def __init__(self, Fid, rank, Fdate, Fcomment, Feedback_giver, bid):
        self.Fid = Fid
        self.rank = rank
        self.Fdate = Fdate
        self.Fcomment = Fcomment
        self.Feedback_giver = Feedback_giver
        self.bid = bid
    def _feedback_info(self):
        self.result = {}
        self.result = {'Fid':self.Fid, 'Feedback_giver': self.Feedback_giver, "Fcomment":self.Fcomment}
        return self.result

    def get_key(self):
        return "Fid"+self.Fid

class usefulness_rating:
    def __init__(self, Fid, score, userid):
        self.Fid = Fid
        self.score = score
        self.userid = userid

class orders:
    def __init__(self,Odate, copynum, userid, bid):
        self.Odate = Odate
        self.copynum = copynum
        self.userid = userid
        self.bid = bid

class record_transaction:
    def __init__(self, Tid, Tdate, copynum, bid):
        self.Tid = Tid
        self.Tdate = Tdate
        self.copynum = copynum
        self.bid = bid