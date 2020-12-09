import pprint
from itertools import combinations


def read_input():
    with open("input", "rt") as fd:
        return [int(i) for i in fd.read().splitlines()]


def ngrams(s, n):
    if len(s) < n:
        return []
    else:
        return list(zip(*[s[i:] for i in range(n)]))


def sum_to(t):
    def st(a):
        if sum(a) == t:
            return a

    return st


def valid_number(s, n):
    if [i for i in filter(sum_to(n), combinations(s, 2))]:
        return True
    return False


def part1(s, pre):
    for ng in ngrams(s, pre + 1):
        if not valid_number(ng[:-1], ng[-1]):
            return ng[-1]


def part2(s, pre):
    es = s
    t = part1(s, pre)
    r = 2
    while r:
        for ng in (ngrams(s, r)):
            if sum(ng) == t:
                return max(ng) + min(ng)
        r += 1


test = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102,
        117, 150, 182, 127, 219, 299, 277, 309, 576]

part1(test, 5)
part2(test, 5)
