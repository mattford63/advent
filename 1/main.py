import pprint
from itertools import combinations


def read_entries():
    with open("input", "rt") as fd:
        return [int(i) for i in fd.read().splitlines()]


def sum_to(t):
    def st(a):
        if sum(a) == t:
            return a

    return st


def multiply(a):
    m = 1
    for i in a:
        m = m * i
    return m


def expense_findings(st, list, comb):
    return [multiply(i) for i in filter(sum_to(st), combinations(list, comb))]


entries = read_entries()

pprint.pp(expense_findings(2020, entries, 2))
pprint.pp(expense_findings(2020, entries, 4))
