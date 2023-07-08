# Write a simple program that gets a number from the user and then uses the assert
# statement to raise an exception if the number is zero. Test to make sure that the
# assert statement fires; then turn it off, using one of the methods mentioned in this
# section.


num = int(input('Enter a number: '))
assert num != 0, 'Can not accept zero!'

# to run with __debug__ = false:
# python -O '.\Chapter14\3- Try this - The assert statement.py'

# Or export PYTHONOPTIMIZE=1
# python '.\Chapter14\3- Try this - The assert statement.py'
# To reset: export PYTHONOPTIMIZE=0
