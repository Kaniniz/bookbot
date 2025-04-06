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

