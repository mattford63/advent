import tokenize
from operator import add, sub
from tokenize import NAME, NEWLINE, NUMBER, OP, STRING


def read_input():
    global program
    with tokenize.open('input') as fd:
        tokens = tokenize.generate_tokens(fd.readline)
        i = 1
        program = {}
        for num, value, _, _, _ in tokens:
            if num == NAME:
                program[i] = [value]
            if num == OP:
                program[i].append(value)
            if num == NUMBER:
                program[i].append(int(value))
            if num == NEWLINE:
                i += 1


def parse(line):
    cmd, op, num = line

    if op == '+':
        opf = add
    if op == '-':
        opf = sub

    if cmd == 'nop':
        def nop():
            global ep, state
            ep += 1

        return nop

    if cmd == 'acc':
        def acc():
            global ep, state
            ep += 1
            state = opf(state, num)
        return acc

    if cmd == 'jmp':
        def jmp():
            global ep, state
            ep = opf(ep, num)

        return jmp


def compilep(program):
    return {i: parse(j) for i, j in program.items()}


def init(ep_=1, state_=0, i_=1, visited_=set()):
    global exe, ep, state, i, visited
    exe = compilep(program)
    ep = ep_
    state = state_
    visited = visited_.copy()
    i = i_


def step():
    global i, ep, state, visited
    if ep in visited:
        return False
    else:
        visited.add(ep)
        exe[ep]()
        i += 1
        return True


def run():
    while step():
        print(i, ep, state)
        pass
