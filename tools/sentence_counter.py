def sent_count():

    from tools.file_manager import punc, x, content, new, word_list

    count = len([i for i in new if i in punc])
    print("The number of sentences in the input :", count)