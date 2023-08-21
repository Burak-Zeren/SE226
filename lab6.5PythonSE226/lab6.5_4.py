word_list = ["iceman", "nemaic", "burak", "car", "google", "apple", "maenci"]
def anagrams(word, word_list):
    sorted_list=[]
    newItem=sorted(str(word.lower().replace(" ", "")))
    for wordOfList in word_list:
        newWord=sorted(str(wordOfList).lower().replace(" ",""))
        if newWord == newItem:
            sorted_list.append(wordOfList)
    return sorted_list
print(anagrams("cinem A",word_list))
