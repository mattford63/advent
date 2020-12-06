from functools import reduce


def to_set(lol):
    return [set(l) for l in lol]


def union(a, b):
    return a | b


def intersection(a, b):
    return a & b


def part1(lol):
    return len(reduce(union, to_set(lol)))


def part2(lol):
    return len(reduce(intersection, to_set(lol)))


def read_input(part_func):
    with open("input", "rt") as fd:
        return sum([part_func(x)
                    for x in [p.split() for p in fd.read().split("\n\n")]])


read_input(part1)
read_input(part2)
