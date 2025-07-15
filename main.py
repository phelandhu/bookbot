import json
import sys
from stats import get_num_words
from stats import get_character_count
from stats import sort_list



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    list_letters = get_character_count(book_text)
    word_list = sort_list(list_letters)
#    print(list_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in word_list:
        r = json.dumps(x)
        loaded_r = json.loads(r)
        print(loaded_r['char']+": "+str(loaded_r['num']))
    
#    print(word_list)
    print("============= END ===============")


main()
