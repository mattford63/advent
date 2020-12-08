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
            global ep
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
            global ep
            ep = opf(ep, num)
        return jmp


def compilep(program):
    return {i: parse(j) for i, j in program.items()}


def init(ep_=1, state_=0, i_=1, visited_=set()):
    """ Resets global state and compiles the code"""
    global exe, ep, state, i, visited
    exe = compilep(program)
    ep = ep_
    state = state_
    visited = visited_.copy()
    i = i_


def step():
    global i
    if ep in visited:
        return False
    else:
        visited.add(ep)
        exe[ep]()
        i += 1
        return True


def run():
    global path
    path = []
    while step():
        if ep >= len(program):
            print("Prog termianted: ",i, ep, state)
            return True
        if trace(ep):
            path.append(ep)
        else:
            pass
    print("Prog infinite loop: ", i, ep, state)
    return False


def trace(ep):
    return program[ep][0] == 'jmp' or program[ep][0] == 'nop'


def swap_run():
    for c in path:
        orig = program[c][0]
        swapped = False
        if orig == 'jmp':
            program[c][0] = 'nop'
            swapped = True
        if orig == 'nop':
            program[c][0] = 'jmp'
            swapped = True
        if swapped:
            init()
            if run():
                break
            else:
                program[c][0] = orig


read_input()
init()
run()
swap_run() # uses the path set in the previous run (list of jumps and noops)
