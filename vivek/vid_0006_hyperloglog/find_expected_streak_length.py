from itertools import product
import math
import random
import sys

GAMMA = 0.577

def expected_streak_length_by_formula(n):
    #return math.log2(n/2) + GAMMA/0.693 - 0.5
    return math.log2(n) - 0.67

def find_max_streak(s):
    count = 0
    mx = 0
    for ht in s:
        if ht == 'H':
            count += 1
            mx = max(mx, count)
        else:
            count = 0
    return mx

def expected_streak_length(n):
    if n > 19:
        return -1
    seqs = product('HT', repeat=n)
    s = 0
    nums = 0
    for seq in seqs:
        seq = ''.join(seq)
        s += find_max_streak(seq)
        nums += 1

    return s / nums

def statistically(n):
    s = 0
    NUM_EXPERIMENTS = 10000
    for _ in range(NUM_EXPERIMENTS):
        max_streak, streak = 0, 0
        for _ in range(n):
            toss = 'H' if random.randint(0, 1) == 0 else 'T'
            if toss == 'H':
                streak += 1
                max_streak = max(streak, max_streak)
            else:
                streak = 0
        s += max_streak
    return s / NUM_EXPERIMENTS

print("idx formulaic statistically")
for i in range(20, 200):
    #e1 = expected_streak_length(i)
    e2 = expected_streak_length_by_formula(i)
    e3 = statistically(i)
    fmt = "{:2}  {:4f}  {:4f}"
    print(fmt.format(i, e2, e3))
