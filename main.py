import sys

from stats import get_book_text, get_char_num, sort_chars


def main(args):
    if not len(args) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(args[1])

    num_words = len(text.split())

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
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


main(sys.argv)
