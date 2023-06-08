# Consider a variable width that’s in the module make_window.py. In which of the
# following contexts is width in scope?:
# (A) within the module itself ------> ok
# (B) inside the resize() function in the module -------> not ok
# (C) within the script that imported the make_window.py module ------> ok if : from make_window import *
