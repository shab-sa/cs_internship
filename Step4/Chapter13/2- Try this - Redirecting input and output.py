# Write some code to use the mio.py module in listing 13.1 to capture all the print output
# of a script to a file named myfile.txt, reset the standard output to the screen, and print
# that file to screen.

import mio
def main():
    mio.capture_output(file='myfile.txt')
    print('I am testing the print output')
    mio.restore_output()
    mio.print_file(file='myfile.txt')

if __name__=='__main__':
    main()