from alphabet_order import ap_orf
from long_words import lg_wdf
from top_words import tp_wdf

def main():
    print("Welcome to my program!")
    while True:
        user_input = input("Please select what you want to do with your text: \nTop 5 words by usage frequency [tw] \nTop 5 words by length [lw]\nAll words sorted in alphabetic order [ao]\nExit [e]\n")
        user_input = user_input.lower()
        if user_input == "tw" or user_input == "lw" or user_input == "ao":
            print("Okay, input your text below:")
            text = input()
            if user_input == "tw":
                top_words = tp_wdf(text)
                for i, w in enumerate(top_words):
                    print(f"Number {i+1}: \"{w['countable']}\" has been used {w[str('count')]} time(s)")
            elif user_input == "lw":
                long_words = lg_wdf(text)
                for i, w in enumerate(long_words):
                    print(f"Number {i+1}: \"{w['countable']}\" has {w[str('length')]} letters")
            elif user_input == "ao":
                result = ap_orf(text)
                result = ", ".join(result)
                print(f"These are the words in aplabetic order: {result}")
        elif user_input == "e":
            print("Goodbye!")
            break
        else:
            print("Invalid answer.")
            continue
if __name__ == "__main__":
    main()