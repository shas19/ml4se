from python_graphs import program_graph
from python_graphs import program_graph_graphviz
import pygraphviz


with open('example.py') as f:
    fn = f.read()

graph = program_graph.get_program_graph(fn)
gg = program_graph_graphviz.to_graphviz(graph)

gg.draw('graph.png', prog='neato')


print(dir(graph))
print(graph.to_ast())