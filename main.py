from stats import count_words
from stats import get_word_count

def get_book_text(file_path):
    with open(file_path) as file:
        book = file.read()
        return book

def main():
    print(f"{count_words(get_book_text('books/frankenstein.txt'))} words found in the document")
    print(get_word_count(get_book_text('books/frankenstein.txt')))

main()