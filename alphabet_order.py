def ap_orf(text):
    text_list = text.split()
    words = []
    unique_words = []
    for i in text_list:
        word = i.lower().replace(',','').replace('.','').replace(':','').replace(';','').replace('=','').replace('/','').replace('(','').replace(')','')
        words.append(word)
        if word in unique_words:
            continue
        else:
            if len(word) > 3:
                unique_words.append(word)
    unique_words.sort()
    result = []
    for i in unique_words:
        result.append(i)
    return result
def main():
    text = input()
    result = ap_orf(text)
    result = ", ".join(result)
    print(f"Words in aplabetic order: {result}")
if __name__ == "__main__":
    main()
