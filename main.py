from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text


def main():
    text_block = get_book_text("books/frankenstein.txt")
    #print(text)
    count = get_num_words(text_block)
    print(count)


main()
