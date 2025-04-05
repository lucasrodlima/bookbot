from stats import get_book_text, get_char_num


def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = len(text.split())

    print("============ BOOKBOT ============")

    print(f"{num_words} words found in the document")

    chars = get_char_num(text)

    print(chars)


main()
