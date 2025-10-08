from random import randint

alphabet = ["A", "C", "G", "T", ""]
patterns = ["ATTAGA", "ΑCGCΑTΤT", "ΑGGACTCAA", "ATTTCAGT"]

a_min, a_max = 1, 3
b_min, b_max = 1, 2
c_min, c_max = 1, 2


def generate_string():
    out = ""

    # part a
    a_count = randint(a_min, a_max)
    for _ in range(0, a_count):
        out += alphabet[randint(0, 3)]

    # part b
    for p in patterns:
        mutated = p
        b_count = randint(b_min, b_max)
        for _ in range(0, b_count):
            idx = randint(1, len(mutated) - 1)
            mutated = (
                mutated[:idx] + alphabet[randint(0, 4)] + mutated[idx + 1 :]
            )
        out += mutated

    # part c
    c_count = randint(c_min, c_max)
    for _ in range(0, c_count):
        out += alphabet[randint(0, 3)]

    return out
