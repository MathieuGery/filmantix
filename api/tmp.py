def deleteCopy(tab: list) -> dict:
    dic = {}
    for i, word in enumerate(tab):
        word = str(word)
        if word in dic:
            dic[word].append(i)
        else :
            dic[word] = [i]
    return dic
