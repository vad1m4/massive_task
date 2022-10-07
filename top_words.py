def key(e):
    return e['count']
def tp_wdf(text):
    text_list = text.split()
    words = []
    unique_words = []
    top_words = []
    for i in text_list:
        word = i.lower().replace(',','').replace('.','').replace(':','').replace(';','').replace('=','').replace('/','').replace('(','').replace(')','')
        words.append(word)
        if word in unique_words:
            continue
        else:
            unique_words.append(word)
    for i in range(0, len(unique_words)):
        count = 1
        countable = unique_words[i]
        count = words.count(countable)
        top_words.append({"countable": countable, "count": count})
    top_words.sort(reverse=True, key=key)
    del top_words[5:]
    return top_words
def main():
    text = input()
    top_words = tp_wdf(text)
    for i, w in enumerate(top_words):
        print(f"Number {i+1}: {w['countable']} has been used {w[str('count')]} time(s)")
if __name__ == "__main__":
    main()