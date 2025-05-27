from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        filepath = sys.argv[1]

        text_block = get_book_text(filepath)
        #print(text)
        word_count = get_num_words(text_block)
        #print(count)
        
        char_count = get_char_count(text_block)
        #print(char_count)

        #OUTPUT =============================================
        print("============ BOOKBOT ============" '\n' "Analyzing book found at books/frankenstein.txt...")
        print(f"----------- Word Count ---------- \n{word_count}")
        print("--------- Character Count -------")
        print_report(char_count)
        print("============= END ===============")
    return sys.exit(0)

main()
