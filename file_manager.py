punc = ".", "!", "?", ":"

x = open('text_input.txt', 'r')
content = x.read()
new = content.replace("\n", " ")
word_list = new.split(" ")