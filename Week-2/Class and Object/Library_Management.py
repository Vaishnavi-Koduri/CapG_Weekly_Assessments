class Book:
    def __init__(self,book_name,author_name,isbn_num):
        self.book_name= book_name
        self.author_name= author_name
        self.isbn_num= isbn_num

    def title(self,book_name):
        print(f"The title of the book is: {book_name}")

    def author(self,author_name):
        print(f"The author of the book is: {author_name}")

    def isbn(self,isbn_num):
        print(f"The isbn number of the book is: {isbn_num}")

book= Book("Harry Potter: Chamber of secrets","JK Rowling",2893833)
book.title("Harry Potter: Chamber of secrets")
book.author("JK Rowling")
book.isbn(2893833)