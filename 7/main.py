import re
import networkx as nx
import pygraphviz as pgv


def read_input():
    with open('input') as fd:
        for l in fd.read().splitlines():
            add_line_to_graph(l)


def add_line_to_graph(l):
    n, nodes = l.split("contain")
    nodes = nodes.split(',')
    n = re.match('(.*) bag', n)[1]

    if nodes[0] == " no other bags.":
        G.add_node(n)
    else:
        def add_edges(n, node):
            r = re.match('.*(\d+) (.*) bag.*', node)
            G.add_edge(r[2], n, count=int(r[1]))

        for node in nodes:
            add_edges(n, node)


G = nx.DiGraph()
read_input()

part1 = len(nx.dfs_tree(G, 'shiny gold')) - 1


def sum_of_bags(node):
    c = 1
    for k, v in G.pred[node].items():
        c = c + v['count'] * sum_of_bags(k)
    return c


part2 = sum_of_bags('shiny gold') - 1


nx.nx_agraph.to_agraph(G).write('bags.dot')
