from stats import get_num_words
from stats import get_num_chars
from stats import sorted_dict_list
import sys

if len(sys.argv) < 2:
    print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

try:
    with open(path_to_book, 'r') as book:
        content = book.read()
        print(content)
except BookNotFoundError:
    print(f"Error: File '{path_to_book}' not found.")

#path_to_file = "./books/frankenstein.txt"

def main(f_path):
    #print(get_book_text(f_path))
    #print(f"{get_num_words(f_path)} words found in the document")
    #print(get_num_chars(f_path))
    
    #print(sorted_dict_list(f_path).isalpha())
    print("============ BOOKBOT ============\n"
    f"Analyzing book found at {sys.argv[1]}...\n"
    "----------- Word Count ----------\n"
    f"Found {get_num_words(f_path)} total words\n"
    "--------- Character Count -------")
    for dic in sorted_dict_list(f_path):
        if dic["char"].isalpha():
            print(f"{dic['char']}: {dic['count']}")


main(path_to_book)