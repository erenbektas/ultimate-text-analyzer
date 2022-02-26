#- Counting words
#- Counting sentences
#- Counting lines
#- Identifying palindromes
#- Reading the text from a text file

punc = ".", "!", "?", ":"
x = input("Enter the text here: ")

list = x.split()
number_of_words = len(list)
print(number_of_words)

count = len([i for i in x if i in punc])
print(count)