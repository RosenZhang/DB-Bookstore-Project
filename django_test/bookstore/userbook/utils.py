from django.db import connection
def get_book_list():
    cursor = connection.cursor()
    cursor.execute('SELECT title FROM DBproject.catalog_book')
    titles = [row[0] for row in cursor.fetchall()]
    #db.close()
    return titles