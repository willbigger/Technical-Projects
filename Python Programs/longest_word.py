def longest_word(sen):
    order = 0
    sen = list(sen)
    for i in range(len(sen)):
        if ((33 <= ord(sen[order])) and (ord(sen[order]) <= 64)) \
                or ((91 <= ord(sen[order])) and (ord(sen[order]) <= 96)) \
                or ((123 <= ord(sen[order])) and (ord(sen[order]) <= 126)):
            sen[order] = ""
        order += 1
    sen = ''.join(sen)
    sen = sen.split(" ")
    return max(sen, key=len)
