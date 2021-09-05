import numpy as np


def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0, 1], p=[1 - p1, p1], size=10000)
    return seq


def count(seq):
    c = 0
    for i in range(len(seq[:-4])):
        if list(seq[i:i + 5]) == [1, 1, 1, 1, 1]:
            c += 1
    return c


def main(p1):
    seq = generate(p1)
    return count(seq)


print(main(2 / 3))
