from collections import Counter
import re
def most_common_word(Book):
    # Remove punctuation marks
    Book=re.sub(r'[^\w\s]', '', Book.lower())
    most = Book.split()
    hash=set()
    #to check if empty string return empty string
    if not most:
         return "Empty string"
    for word in most:
        if word in most:
            continue
        else:
            hash.add(word)
    counter = Counter(most)
    most_repeat = counter.most_common()
    return most_repeat[0][0]
words = "John is the son of John second, Second son. of John second is William second"
print(most_common_word(words))


