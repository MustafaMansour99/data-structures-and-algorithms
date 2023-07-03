def repeated_word(strings):
    list_splits=strings.split(" ")
    list=[]
    for word in list_splits:
        if word not in list:
            list.append(word)
        else:
            return word
    return "No Repetition"


words="hi abdullah mustafa hi abdullah"
print(repeated_word(words))