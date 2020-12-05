import math


def cmd(r, c):
    d = (r[1] - r[0]) / 2
    if any(c == s for s in ["B", "R"]):
        return math.ceil(r[0] + d), r[1]
    if any(c == s for s in ["F", "L"]):
        return r[0], math.floor(r[1] - d)


def run_cmds(r, cs):
    if r[0] == r[1]:
        return r[0]
    else:
        return run_cmds(cmd(r, cs[0]), cs[1:])


def seat_pos(cs):
    row = run_cmds((0, 127), cs[:7])
    col = run_cmds((0, 7), cs[7:])
    return row, col


def seat_id(pos):
    return pos[0] * 8 + pos[1]


def seat_ids():
    with open("input") as fd:
        return [seat_id(seat_pos(cs)) for cs in [l for l in fd.read().splitlines()]]


def find_gap(l):
    if l[0] + 1 != l[1]:
        return l[0] + 1
    else:
        return find_gap(l[1:])


def part1():
    return max(seat_ids())


def part2():
    return find_gap(sorted(seat_ids()))
