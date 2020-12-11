# Push down automata - FSM
ads = [16,  10,  15,  5,  1,  11,  7,  19,  6,  12,  4,  9, 18, 21, 22]
starting_stack = (1, 0)  # (1=on|0=off ,jolts)
#states = {0, 1}


def read_input():
    with open("input") as fd:
        return [int(l) for l in fd.read().splitlines()]


def plug_in(stack, adapter):
    if (adapter - stack[1]) <= 3 and (adapter - stack[1]) >= 1 and stack[0] == 1:
        return (1, adapter)
    else:
        return (0, adapter)


def prep_adapters(adapters):
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters


def find(adapters, stack):
    acc = [0]  # fudge the accumulator
    for a in adapters:
        acc.append(a)
        if plug_in(stack, a)[0]:
            stack = plug_in(stack, a)
    return acc


def ngrams(s, n):
    if len(s) < n:
        return []
    else:
        return list(zip(*[s[i:] for i in range(n)]))


def dist(a):
    return list(map(lambda t: t[1] - t[0], ngrams(a, 2)))


def part1(adapters):
    a = prep_adapters(adapters.copy())
    d = dist(find(a, starting_stack))
    print(d)
    return d.count(1) * d.count(3)


def part2(adapters):
    li = prep_adapters(adapters.copy())
    routes = {}
    routes[0] = 1
    for num in li:
        routes[num] = routes.get(num-1, 0) + \
            routes.get(num-2, 0) + \
            routes.get(num-3, 0)

    return routes[li[-1]]


memo = {}


def part2a(adapters):
    a = prep_adapters(adapters.copy())
    xs = find(a, starting_stack)

    def route(i):
        if i == len(xs)-1:
            return 1
        ans = 0

        if i in memo:
            return memo[i]

        for j in range(i+1, len(xs)):
            if xs[j] - xs[i] <= 3:
                ans += route(j)
            else:
                break
        memo[i] = ans
        return ans


    return route(0)


#part2a(ads)
