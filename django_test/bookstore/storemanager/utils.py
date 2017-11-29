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

def get_orders_info(Odate,userid,bid):
    orders_info = my_custom_sql_dict("select * from orders where Odate = '%s', userid ='%s', bid ='%s'" %(Odate,userid,bid))
    orders_info_save_to_class = orders(**orders_info)
    fetched_class.register_class(orders_info_save_to_class)
    print
    "\n\n =============dictionary info================", orders_info_save_to_class._orders_info()
    return orders_info_save_to_class._orders_info()
