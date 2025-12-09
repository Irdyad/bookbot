from stats import *
import sys

#PATH_TO_BOOK = "books/frankenstein.txt"

def main() -> int:

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    PATH_TO_BOOK = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path}...")
    book_content = get_book_text(PATH_TO_BOOK)

    print("----------- Word Count ----------")
    num_words = count_words(book_content)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    letter_count = count_char(book_content)
    letter_count = dict_to_list(letter_count)
    letter_count.sort(reverse=True, key=sort_on)
    print_list_dict(letter_count)

    print("============= END ===============")



def get_book_text(path: str) -> str:
    with open(path) as b:
        book_contents = b.read()
    
    return book_contents

def print_list_dict(items: list) -> None:
    for item in items:
        print(f"{item["char"]}: {item["num"]}")

def sort_on(items):
    return items['num']

main()