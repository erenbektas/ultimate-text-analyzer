# - Counting words
# - Counting sentences
# - Counting lines
# - Identifying palindromes
# - Reading the text from a text file

import string

punc = ".", "!", "?", ":"

x = open('Text_input.txt', 'r')
content = x.read()

# count number of words in the input

new = content.replace("\n", " ")
word_list = new.split(" ")
print(word_list)
number_of_words = len(word_list)
print("The number of words in the input is", number_of_words, ".")

# count number of sentences in the input

count = len([i for i in new if i in punc])
print("The number of sentences in the input is", count, ".")

list_of_lines = content.split("\n")
number_of_lines = len(list_of_lines)
print("The number of lines in the input is", number_of_lines, ".")

# list of palindromes in the file

list_of_palindromes = []
for n in word_list:
    if n[-1] not in string.punctuation:
        if n == n[::-1]:
            list_of_palindromes.append(n)
    else:
        no_punc = n[:-1]
        if n[:-1] == no_punc[::-1]:
            list_of_palindromes.append(no_punc)

print("Palindromes in the input are", list_of_palindromes)

# read the text

print("Content:",content)
