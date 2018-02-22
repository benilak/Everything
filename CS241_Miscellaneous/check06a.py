class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = int()

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Publication Year: ")

    def display_book_info(self):
        print("\n{} ({}) by {}".format(self.title, self.publication_year, self.author))


class TextBook(Book):
    def __init__(self):
        self.subject = ""
        super().__init__()

    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print("Subject: {}".format(self.subject))


class PictureBook(Book):
    def __init(self, illustrator):
        self.illustrator = illustrator
        super().__init__()

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print("Illustrated by {}".format(self.illustrator))


def main():
    book = Book()
    book.prompt_book_info()
    book.display_book_info()

    print()
    textbook = TextBook()
    textbook.prompt_book_info()
    textbook.prompt_subject()
    textbook.display_book_info()
    textbook.display_subject()

    print()
    picturebook = PictureBook()
    picturebook.prompt_book_info()
    picturebook.prompt_illustrator()
    picturebook.display_book_info()
    picturebook.display_illustrator()


if __name__ == "__main__":
    main()
