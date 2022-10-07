def key(e):
    return e['length']
def lg_wdf(text):
    text_list = text.split()
    words = []
    unique_words = []
    long_words = []
    for i in text_list:
        word = i.lower().replace(',','').replace('.','').replace(':','').replace(';','').replace('=','').replace('/','').replace('(','').replace(')','')
        words.append(word)
        if word in unique_words:
            continue
        else:
            unique_words.append(word)
    for i in range(0, len(unique_words)):
        countable = unique_words[i]
        length = len(unique_words[i])
        long_words.append({"countable": countable, "length": length})
    long_words.sort(reverse=True, key=key)
    del long_words[5:]
    return long_words
def main():
    text = input()
    long_words = lg_wdf(text)
    for i, w in enumerate(long_words):
        print(f"Number {i+1}: {w['countable']} has {w[str('length')]} letters")
if __name__ == "__main__":
    main()