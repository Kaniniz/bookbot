def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    letters = count_letters(text)
    make_report_of_text(book_path)
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    text = text.split()
    return len(text)

def count_letters(text):
    text = text.lower()
    letters = {}
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters

def make_report_of_text(book_path):
    text = count_letters(get_book_text(book_path))     
    words = count_words(get_book_text(book_path))
    alpha_text_list = []
    for i in text:
        if i.isalpha():
            alpha_text_list.append(i)
    alpha_text_list.sort()

    print(f"Generating report...")
    print(f"{words} words in the text.")
    for item in alpha_text_list:
        print(f"Letter {item} was found {text[item]} times")

main()