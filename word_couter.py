with open('./output.txt', mode ='wt', encoding = 'utf-8') as file:
    word_string = file.read()

word_dict = {}

for word in word_string:
    if word not in word:
        word_dict.setdefault(word, default = 0)
    else:
        word_dict[word] += 1
