import sqlite3
from .database_connection import *


def create_book_table():
    connection = DatabaseConnection('data.db')
    cursor = connection.cursor()
    connection.execute('create table books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()


def add_book(name, author):
    with open(book_file, 'a') as books:
        books.write(f'{name},{author},0 \n')


def list_all_books():
    with open(book_file, 'r') as books:
        pass


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = 1
    save_all_books(books)


def get_all_books():
    with open(book_file, 'r') as books:
        lines = [book.strip().split(',') for book in books.readlines()]
    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


def save_all_books(books):
    with open(book_file, 'w') as file:
        for book in books:
            file.write(f"{'name': book['name'], 'author': book['author'], 'read': book['read'] \n}")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    save_all_books(books)
