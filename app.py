from utils.database import add_book, list_all_books, mark_book_as_read, delete_book

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete the book
- 'q' to quit
"""


def menu():
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            prompt_list_all_books()
        elif user_input == 'r':
            prompt_mark_book_as_read
        elif user_input == 'd':
            delete_book(input('Enter the name of the book from the list which you want to delete'))
        else:
            user_input = input("Sorry ! You have entered an incorrect book name. Please enter again, enter 'q' to quit")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    inputs = input("Enter the name and author of the book").split(',')
    add_book(inputs[0], inputs[1])


def prompt_list_all_books():
    books = list_all_books()
    for book in books:
        print(f'{book}')


def prompt_mark_book_as_read():
    mark_book_as_read(input('Enter the book from the list which you have already read'))


def prompt_delete_book():
    delete_book(input('Enter the name of the book from the list which you want to delete'))


menu()
