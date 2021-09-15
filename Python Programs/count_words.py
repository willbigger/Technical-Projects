def count(paragraph):
    words = {}
    list_words = paragraph.split(" ")
    for word in list_words:
        if word in words:
            words[word.lower()] += 1
        else:
            words[word.lower()] = 1
    return words
