# - Counting words
# - Counting sentences
# - Counting lines
# - Identifying palindromes
# - Reading the text from a text file

punc = ".", "!", "?", ":"

x = open('Text_input.txt', 'r')
content = x.read()

# count number of words in the input

word_list = content.split(" ")
number_of_words = len(word_list)
print("The number of words in the input is", number_of_words, ".")

# count number of sentences in the input

count = len([i for i in content if i in punc])
print("The number of sentences in the input is", count, ".")

list_of_lines = content.split("\n")
number_of_lines = len(list_of_lines)
print("The number of lines in the input is", number_of_lines, ".")
