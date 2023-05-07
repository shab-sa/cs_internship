def distance(strand_a, strand_b):
    s = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for i, c in enumerate(strand_a):
        if strand_b[i] != c:
            s += 1
    return s