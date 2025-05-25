def get_num_words(text):
    word_count = 0
    words = text.split()
    #print(words)
    for word in words:
        word_count += 1
    return f'{word_count} words found in the document'