# def repeated_word(strings):
#     list_splits=strings.split(" ")
#     list=[]
#     for word in list_splits:
#         if word not in list:
#             list.append(word)
#         else:
#             return word
#     return "No Repetition"


# words="hi abdullah mustafa hi abdullah"
# print(repeated_word(words))

"""
in this function handle if there is 2 words duplicated in same sentence in another way
"""
def repeated_word(strings):
    list_splits = strings.lower().split(" ")
    word_count = {}
    
    for word in list_splits:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

        if word_count[word] == 2:
            return word
    
    return "No Repetition"


words = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
print(repeated_word(words))