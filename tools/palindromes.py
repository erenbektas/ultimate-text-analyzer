def palind():

    import string

    from tools.file_manager import punc, x, content, new, word_list

    list_of_palindromes = []
    for n in word_list:
        if n[-1] not in string.punctuation:
            if n == n[::-1]:
                list_of_palindromes.append(n)
        else:
            no_punc = n[:-1]
            if n[:-1] == no_punc[::-1]:
                list_of_palindromes.append(no_punc)

    print("Palindromes in the input             :", ", ".join(list_of_palindromes))
    print("\n")