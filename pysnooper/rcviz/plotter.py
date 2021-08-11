import itertools
import ntpath
from typing import Tuple, List

import graphviz

from pysnooper.rcviz.trace_node import TraceNode


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def plot_graph(list_graph: List[Tuple[TraceNode, TraceNode]],
               filename='reviz.png',
               shape='Mrecord'):
    """https://graphviz.readthedocs.io/en/stable/manual.html"""
    filename_leaf = path_leaf(filename)
    name, _format = filename_leaf.split('.')
    format_dict = lambda d: '(' + ', '.join([f'{k}={v}' for k, v in d.items()]) + ')'
    g = graphviz.Digraph(name, filename=filename, format=_format)

    for tn in itertools.chain(*list_graph):
        label = format_dict(tn.kwargs).replace('{', '').replace('}', '').replace('|', '')
        label = "{{" + tn.function_name + "}" + "|" + label + "}"
        g.node(tn.id, shape=shape, label=label)

    for e1, e2 in list_graph:
        g.edge(e1.id, e2.id, label=e2.return_val, color='grey', fontsize='10')
    g.render(filename=filename.strip(f'.{_format}'), cleanup=True)

