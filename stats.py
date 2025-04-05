def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents


def get_char_num(text):
    chars = {}

    for char in text:
        if char == " " or char == "\t" or char == "\n":
            continue
        elif char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1

    return chars


def sort_chars(chars):
    sorted = []

    for char in chars:
        if char.isalpha():
            sorted.append({"char": char, "num": chars[char]})

    def sort_on(dict):
        return dict["num"]

    sorted.sort(reverse=True, key=sort_on)

    return sorted
