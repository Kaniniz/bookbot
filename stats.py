def get_book_text(file_path):
    with open(file_path) as file:
        book = file.read()
        return book

def count_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def get_word_count(text):
    word_count = {}
    lowerd = text.lower()
    words = lowerd.split()
    for word in words:
        for l in word:
            if l in word_count:
                word_count[l] += 1
            else:
                word_count[l] = 1
            
    return word_count

def sort_on(dict):
    return dict["num"]


def sort_dict(dict):
    sorted = []
    for i in dict:
        temp = {}
        temp["name"] = i
        temp["num"] = dict[i]
        sorted.append(temp)
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def generate_report(file_path):
    text = get_book_text(file_path)
    words = get_word_count(text)
    sorted_words = sort_dict(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for I in sorted_words:
        print(f"{I['name']}: {I['num']}")
    print("============= END ===============")