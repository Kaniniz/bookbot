def get_book_text(file_path):
    with open(file_path) as file:
        book = file.read()
        return book

def main():
    print(get_book_text("books/frankenstein.txt"))

main()