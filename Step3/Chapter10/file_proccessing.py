
import string


def clean_file(file_name, clean_file_name):
    with open(file_name) as infile, open(clean_file_name, "w") as outfile:
        for line in infile:
            # make all one case
            line = line.lower()
            # remove punctuation
            table = line.maketrans('', '', string.punctuation)
            line = line.translate(table)
            # split into words
            cleaned_words = line.split()
            # write all words for line
            for cleaned_word in cleaned_words:
                outfile.write(cleaned_word+'\n')


def words_count(file_name):
    with open(file_name) as infile:
        word_count = {}
        for line in infile:
            word_count[line.strip()] = word_count.get(line.strip(), 0)+1
    keys = list(word_count.items())
    keys.sort(reverse=True, key=lambda item: item[1])
    print('Three most frequent words are: ', keys[:3])
    print('Three least frequent words are: ', keys[-3:])
