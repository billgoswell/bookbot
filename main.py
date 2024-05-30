
def main():
    book_path = "books/frankenstein.txt"
    book = get_book_contents(book_path) 
    num_words = count_words(book)
    chars = count_chars(book)
    sorted_letters = sort_letters(chars)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for x in sorted_letters:
        a = x
        b, c = a.popitem()
        print(f"The {b} character was found {c} times")
    print("--- End Report ---")

def sort_letters(dict_chars):
    dict_letters = []
    for x in dict_chars:
        if x.isalpha():
            dict_letters.append({x: dict_chars[x]})
    dict_letters.sort(reverse=True, key = sort_on)
    return dict_letters
    

def sort_on(char):
    x = char.values()
    return list(x)[0]


def count_words(book):
    words = book.split()
    return len(words)

def count_chars(book):
    lowercase_book = book.lower()
    chars = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0,
        "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
        "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0,
        "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, "'": 0, ",": 0,
        "(": 0, ")": 0, ".": 0, "-": 0, ":": 0, ";": 0, "1": 0,
        "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0,
        "9": 0, "0": 0, "[": 0, "]": 0, "#": 0, "*": 0, "?": 0,
        "!": 0, '"': 0, "_": 0, "/": 0, "%": 0, "@": 0, "$": 0, 
        " ": 0, "\n": 0
    }
    for c in lowercase_book:
        chars[c] += 1
    return chars

def get_book_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()

