# If you wanted to check whether a line ends with the string "rejected", what string
# method would you use? Would there be any other ways to get the same result?

x = "It was rejected"
print(x.endswith("rejected"))
print(x.rfind("rejected") == len(x)-8)
print(x[len(x)-8:]=="rejected")
