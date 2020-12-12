def read_input():
    with open('input') as fd:
        return [parse(line) for line in fd.read().splitlines()]
    fd.close()


def parse(str):
    a = list(str)
    return (a[0], int(''.join(a[1:])))


# (x,y,direction)
def elf_compile1(p):
    def N(n):
        return lambda p: (p[0], p[1] + n, p[2])

    def S(n):
        return lambda p: (p[0], p[1] - n, p[2])

    def E(n):
        return lambda p: (p[0] + n, p[1], p[2])

    def W(n):
        return lambda p: (p[0] - n, p[1], p[2])

    def L(n):
        return lambda p: (p[0], p[1], ((p[2] - n) % 360))

    def R(n):
        return lambda p: (p[0], p[1], ((p[2] + n) % 360))

    def F(n):
        def _F(p):
            d = p[2]  # clockwise from east
            if d == 0: return E(n)(p)
            if d == 90: return S(n)(p)
            if d == 180: return W(n)(p)
            if d == 270: return N(n)(p)
        return _F

    e = []
    for l in p:
        cmd, num = l

        if cmd == 'N':
            e.append(N(num))

        if cmd == 'S':
            e.append(S(num))

        if cmd == 'E':
            e.append(E(num))

        if cmd == 'W':
            e.append(W(num))

        if cmd == 'L':
            e.append(L(num))

        if cmd == 'R':
            e.append(R(num))

        if cmd == 'F':
            e.append(F(num))

    return e


def elf_compile2(p):  # (m, n, x, y) (waypoint, boat)
    def N(n):
        return lambda p: (p[0], p[1] + n, p[2], p[3])

    def S(n):
        return lambda p: (p[0], p[1] - n, p[2], p[3])

    def E(n):
        return lambda p: (p[0] + n, p[1], p[2], p[3])

    def W(n):
        return lambda p: (p[0] - n, p[1], p[2], p[3])

    def relative_offset(p):
        return (p[0] - p[2], p[1] - p[3])

    def R(n):
        def _R(p):
            if n == 0:
                return p
            if n == 90:
                return (p[1], -p[0], p[2], p[3])
            if n == 180:
                return (-p[0], -p[1], p[2], p[3])
            if n == 270:
                return (-p[1], p[0], p[2], p[3])

        return _R

    def L(n):
        return R(-n % 360)

    def F(n):
        def _F(p):
            ro = relative_offset(p)
            return (p[0], p[1],
                    p[2] + n * p[0], p[3] + n * p[1])
        return _F

    e = []
    for l in p:
        cmd, num = l

        if cmd == 'N':
            e.append(N(num))

        if cmd == 'S':
            e.append(S(num))

        if cmd == 'E':
            e.append(E(num))

        if cmd == 'W':
            e.append(W(num))

        if cmd == 'L':
            e.append(L(num))

        if cmd == 'R':
            e.append(R(num))

        if cmd == 'F':
            e.append(F(num))

    return e


def elf_run(e, pos):
    print(pos)
    for f in e:
        pos = f(pos)
        print(pos)
    return pos


def manhattan_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


i = read_input()
e = elf_compile1(i)
r = elf_run(e,(0,0,0))
md = manhattan_dist((0, 0), r)


e2 = elf_compile2(i)
r2 = elf_run(e2, (10,1,0,0))
md2 = manhattan_dist((0,0), (r2[2], r2[3]))


#(1,15) -> (1, -15) -> (-15, -1) -> (-1, 15)
