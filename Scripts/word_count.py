import sys
filename = sys.argv[1]
"""  Makes a list of the words in the file filename and the number of times each word appears."""
text_file = open(filename)
words_dic = {}
for line in text_file:         # step through each line in the text file
        for word in line.lower().split():   # split into a list of words
            word = word.strip("'?,.;!-/\"") # strip out the stuff we ignore
            if word not in words_dic:
                words_dic[word] = 0      # add word to words with 0 count
            words_dic[word] = words_dic[word] + 1    # add 1 to the count

text_file.close()
print("List of words in the file with number of times each appears.")
word_list = sorted(words_dic)
for word in word_list:
    print(word, words_dic[word])