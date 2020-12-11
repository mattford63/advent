from copy import deepcopy


def read_input(file):
    with open(file) as fd:
        grid = []
        for i in fd.read().splitlines():
            grid.append(list(i))
        return grid


def direct_adj(g, r, c):
    rc, cc = len(g) - 1 , len(g[0]) -1
    adj = []
    for d in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        if (r + d[0] >= 0 and r + d[0] <= rc) and (c + d[1] >= 0 and c + d[1] <= cc):
            adj.append(g[r + d[0]][c + d[1]])
    return adj


def get_visible_seats(g, r, c):
    rc, cc = len(g) - 1 , len(g[0]) -1
    adj = []
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    def in_boundary (r,c,d):
        return (r + d[0] >= 0 and r + d[0] <= rc) and (c + d[1] >= 0 and c + d[1] <= cc)

    for d in directions:
        od = d
        while in_boundary(r, c, d):
            if is_seat(g, r + d[0], c + d[1]):
                adj.append(g[r + d[0]][c + d[1]])
                break
            else:
                d = (d[0] + od[0], d[1] + od[1])

    return adj


def is_seat(g, r, c):
    return g[r][c] == '#' or g[r][c] == 'L'


def empty(g, r, c):
    return g[r][c] == "L"


def occupied(g, r, c):
    return g[r][c] == '#'


def any_adj_occupied(g, r, c, adj_func):
    return any(i == '#' for i in adj_func(g, r, c))


def x_or_more_adj_occupied(g, x, r, c, adj_func):
    return adj_func(g, r, c).count("#") >= x


def arrive(g, x, r, c, adj_func):
    if empty(g, r, c) and not any_adj_occupied(g, r, c, adj_func):
        return '#'
    if occupied(g, r, c) and x_or_more_adj_occupied(g, x, r, c, adj_func):
        return 'L'
    return g[r][c]


def count_occupied(g):
    return [c == '#' for r in g for c in r].count(True)


def arrivals(g, x, adj_func):
    og = deepcopy(g)
    for r in range(len(og)):
        for c in range(len(og[0])):
            g[r][c] = arrive(og, x, r, c, adj_func)
    if og == g:
        return g
    else:
        arrivals(g, x, adj_func)


tg = read_input('input_test')
ig = read_input('input')

vt1 = read_input('input_viz_test1')
get_visible_seats(vt1, 0, 0)
arrivals(tg, 5, get_visible_seats)
#print(count_occupied(tg))
