from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text


def main():
    text_block = get_book_text("books/frankenstein.txt")
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

main()
