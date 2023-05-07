# In the previous lab, you took the text of the first chapter of Moby Dick, normalized the
# case, removed punctuation, and wrote the separated words to a file. In this lab, you
# read that file, use a dictionary to count the number of times each word occurs, and then
# report the most common and least common words.

word_count = {}


def occur(item):
    return item[1]


with open("moby_01_clean.txt") as infile:
    for line in infile:
        word_count[line.strip()] = word_count.get(line.strip(), 0)+1
keys = list(word_count.items())
keys.sort(reverse=True, key=occur)
print('Three most frequent words are: ', keys[:3])
print('Three least frequent words are: ', keys[-3:])
