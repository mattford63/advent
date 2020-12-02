def read_input():
    with open("./input", "rt") as fd:
        return [parse_line(l) for l in fd.read().splitlines()]


def parse_line(l):
    r, c, p = l.split(" ")
    lb, ub = r.split("-")
    return int(lb), int(ub), c.replace(":", ""), p


def validate_password_p1(t):
    lb, ub, c, p = t
    return p.count(c) >= lb and p.count(c) <= ub


def validate_password_p2(t):
    lb, ub, c, p = t
    lb -= 1
    ub -= 1
    return (p[lb] == c and p[ub] != c) or (p[ub] == c and p[lb] != c)


r1 = filter(validate_password_p1, read_input())
r2 = filter(validate_password_p2, read_input())

print(len(list(r1)))
print(len(list(r2)))
