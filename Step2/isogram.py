def is_isogram(string):
    char_count={}
    for c in string.lower():
        if c.isalpha():
            char_count[c]=char_count.get(c,0)+1
            if char_count[c]>1:
                return False
    return True
