from stats import get_book_text


def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = len(text.split())

    print(f"{num_words} words found in the document")


main()
