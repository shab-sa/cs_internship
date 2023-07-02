# If you look at the man page for the wc utility, you see two commandline
# options that do very similar things. c makes the utility count the bytes in the file, and m
# makes it count characters (which in the case of some Unicode characters can be two or more
# bytes long). In addition, if a file is given, it should read from and process that file, but if
# no file is given, it should read from and process stdin.
# Rewrite your version of the wc utility to implement both the distinction between bytes
# and characters and the ability to read from files and standard input.

import sys


def main():

    mode = 'r'
    file_name = ''
    option = ''

    if len(sys.argv) > 1:
        if sys.argv[1][0] == '-':
            option = sys.argv[1]
        if len(sys.argv) == 3:
            file_name = sys.argv[2]
        else:
            file_name = sys.argv[1]
    if option == '-c':
        mode = 'rb'
    if file_name == '':
        infile = sys.stdin
    else:
        infile = open(file_name, mode)

    line_count = 0
    word_count = 0
    char_count = 0

    for line in infile:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

    if option == '-c':
        print(
            f"File has {line_count} lines, {word_count} words, {word_count} characters")
    if option == '-m':
        print(
            f"File has {line_count} lines, {word_count} words, {word_count} characters")


if __name__ == '__main__':
    main()
