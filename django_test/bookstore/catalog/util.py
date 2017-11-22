from models import Genre
from models import Book

from django.db import connection

def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("select * from catalog_genre;")
        row = cursor.fetchone()
    return row

def try_to_save_a_genre():
    g = Genre(name="sf")
    g.save()

def get_genre_info():
    b = Genre(name='sf')

def get_specific_book():
    return Book.objects.filter(id=1)

def return_all_books():
    all_entries = Book.objects.all()