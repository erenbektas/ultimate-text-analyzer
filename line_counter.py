def line_count():

    from file_manager import punc, x, content, new, word_list

    list_of_lines = content.split("\n")
    number_of_lines = len(list_of_lines)
    print("The number of lines in the input is", number_of_lines, ".")
    print("\n")