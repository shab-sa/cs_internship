# Think about the module you wrote in chapter 9 to count word frequencies. What errors
# might reasonably occur in those functions? Refactor those functions to handle those
# exception conditions appropriately.


import string


class WordCountException(Exception):
    pass


def clean_file(file_name, clean_file_name):
    try:
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
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)


def words_count(file_name):
    try:
        with open(file_name) as infile:
            word_count = {}
            for line in infile:
                word_count[line.strip()] = word_count.get(line.strip(), 0)+1
        keys = list(word_count.items())
        keys.sort(reverse=True, key=lambda item: item[1])
        print('Three most frequent words are: ', keys[:3])
        print('Three least frequent words are: ', keys[-3:])
    except FileNotFoundError as e:
        print(e)
    except IndexError as e:
        print(e)
    except Exception as e:
        print(e)


file_name = "moby_01.txt"
clean_file_name = "moby_01_clean.txt"
clean_file(file_name, clean_file_name)
words_count(clean_file_name)
