from stats import get_book_text, get_char_num, sort_chars


def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = len(text.split())

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    chars = get_char_num(text)

    sorted_chars = sort_chars(chars)

    for char_dict in sorted_chars:
        if not char_dict["char"].isalpha():
            continue
        print(f"{char_dict['char']}: {char_dict['num']}")

    print("============= END ===============")


main()
