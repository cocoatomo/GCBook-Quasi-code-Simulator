# graph.py
import pygraphviz as pgv

G = pgv.AGraph()

G.add_node('root', shape='ellipse')
G.add_node('heap', shape='rect')
G.add_edge('root', 'heap', dir='forward')

G.layout('circo')
G.draw('graph.jpg', format='jpg')
