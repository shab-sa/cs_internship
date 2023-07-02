# Using a shelf object looks very much like using a dictionary. In what ways is using a
# shelf object different? What disadvantages would you expect in using a shelf object?

# the shelve object only accept string as keys while dictionaries have many more options
# like integer, float or booleans. It stores data on disk not in memory.
# I ddoes not support concurrency, disk accesses for large I/o might slow down the program
