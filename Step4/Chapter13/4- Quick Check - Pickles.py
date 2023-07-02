# Think about why a pickle would or would not be a good solution in the following use
# cases:
# Saving some state variables from one run to the next
#     Ok, there is no overlapping runs of program
# Keeping a highscore
#     Ok,
# list for a game
#     Ok
# Storing usernames and passwords
#     Not ok, it is not secure
# Storing a large dictionary of English terms
#     Not ok, loading theh entire pickle into memory
