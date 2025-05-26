def get_num_words(text):
    word_count = 0
    words = text.split()
    #print(words)
    for word in words:
        word_count += 1
    return f'Found {word_count} total words'

def get_char_count(text):
    characters = {}
    text = text.lower()
    words = text.split()
    #print(words)
    count = 1
    for word in words:
        for char in word:
            #characters[char] = count
            if char not in characters:
                characters[char] = count
            else:
                characters[char] += 1
    return characters

def sorting_on(dict1):
    return dict1["num"]

def print_report(dict1):
    list_convert = []
    dict2 = {}
    for key in dict1:
        value = dict1[key]
        if key.isalpha():
            #maybe i dont need two pairs of parenthesis=====================================================================
            list_convert.append(({"char" :key , "num" : value}))
            list_convert.sort(reverse=True, key=sorting_on)
    
    for line in list_convert:
        #messing around trying to add values to new dictionary. Didn't add dictionary in dictionary as intended but there is only one key of everykind because of get_char_count() func so its works.======================================================================================
        dict2[line["char"]] = line["num"]
        #=====================================================================================================================
        print(f'{line["char"]}: {line["num"]}')
