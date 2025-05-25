def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def word_count(text):
    word_count = 0
    words = text.split()
    #print(words)
    for word in words:
        word_count += 1
    return f'{word_count} words found in the document'

def main():
    text_block = get_book_text("books/frankenstein.txt")
    #print(text)
    count = word_count(text_block)
    print(count)


main()
