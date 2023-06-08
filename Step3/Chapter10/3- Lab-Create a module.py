# Package the functions created at the end of chapter 9 as a standalone module. Although
# you can include code to run the module as the main program, the goal should be for the
# functions to be completely usable from another script.

from file_proccessing import *
file_name = "moby_01.txt"
clean_file_name = "moby_01_clean.txt"
clean_file(file_name, clean_file_name)
words_count(clean_file_name)