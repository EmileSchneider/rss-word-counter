def open_file():
    with open('./output.txt', mode ='r', encoding = 'utf-8') as file:
        word_string = file.read()
    return word_string


def gen_word_dict(word_dict, word_string):
    for word in word_string.split():
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

word_string = open_file()   
word_dict = {}
word_dict = gen_word_dict(word_dict, word_string)
