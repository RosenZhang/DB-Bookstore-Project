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

def get_orders_info():
    orders_info = my_custom_sql_dict("select * from orders where ")