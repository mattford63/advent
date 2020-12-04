from copy import deepcopy
from functools import reduce
from operator import mul

# Read input

grid_key = {'.': 0,
            '#': 1}


def parse_line(l):
    return [grid_key[c] for c in l]


def read_input():
    with open("input", "rt") as fd:
        return [parse_line(l) for l in fd.read().splitlines()]


rows = read_input()

# Model
cols = [list(c) for c in zip(*rows)]  # transpose of rows

n_rows = len(rows)
n_cols = len(cols)

init_pos = {'grid': [0, 0],  # cols, rows
            'geog': [0, 0],
            'steps': 0,
            'trees': 0}

init_step = (3, 1)  # across, down

init_bounds = [0, n_rows]  # 0 means infinite


# Logic
def travel(pos, step, bounds):
    if in_bounds(pos, step, bounds):

        pos['geog'][0] += step[0]
        pos['geog'][1] += step[1]

        pos['grid'][0] = pos['geog'][0] % n_cols
        pos['grid'][1] = pos['geog'][1] % n_rows

        pos['trees'] += is_tree(pos)
        pos['steps'] += 1
        return True
    else:
        return False


def is_tree(pos):
    col = cols[pos['grid'][0]]
    return col[pos['grid'][1]]


def in_bounds(pos, step, bounds):
    cb = bounds[0]
    rb = bounds[1]

    c = pos['geog'][0] + step[0] + 1
    r = pos['geog'][1] + step[1] + 1

    return (cb == 0 or c <= cb) and (rb == 0 or r <= rb)


def journey(step):
    pos = deepcopy(init_pos)
    bounds = init_bounds

    while travel(pos, step, bounds):
        pass
    return pos


part1 = journey([3, 1])
part2 = reduce(mul[journey(s)['trees']
                     for s in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]])
