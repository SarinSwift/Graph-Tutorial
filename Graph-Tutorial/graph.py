#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

import queue


class Vertex(object):

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        # add in the vertex(with weight) if it's new
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return self.id + " adjacent to " + [x.id for x in self.neighbors]
        # return f'{self.id} adjacent to {[x.id for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        return self.neighbors[vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        # increment the number of vertices
        self.num_vertices += 1
        # create a new vertex
        new_vertex = Vertex(key)
        # add the new vertex to the vertex list
        self.vert_list[key] = new_vertex
        # return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vert_list:
            return self.vert_list[key]


    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost."""
        # if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)

        # if both vertices in the graph,
        if f in self.vert_list and t in self.vert_list:
        # add the edge by making t a neighbor of f
            self.vert_list[f].add_neighbor(self.vert_list[t], cost)
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vert_list[f].

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_list.keys()

    def breadth_first_search(self, vertex, n):
        """ outputs all nodes that are exactly n connections away from the input node"""

        '''
        properties needed:
            path of nodes array - to store all the current nodes that are n links away from given vertex
            seen dictionary - dictionary that looks like: [vertex: length]
            queue - which stores tuple object that look like: [(vertex, length)]

        pseudocode:
            - start by adding given vertex to the q, and to the seen dictionary
            - loop through while the queue still has vertices
                - pop the item off q and store it in a variable called 'curr'
                - 'curr' is a tuple of (vertex, length)
                - loop through neighbors of curr's vertex
                    - if curr's length + 1 is the given length, we can append the neighbor! in to our path array
                    - additionally, add this neighbor vertex and lenght + 1 to the queue, and the seen array

            - after finding all the neighbors that have a length of the given length, we can return the path array
        '''

        path_nodes = []         # nodes that are n links away from vertex
        seen = [:]              # dictionary of vertex and length that has been visited
        q = queue.Queue()       # queue of tuples of vertex and it's length

        # Push to the queue and update seen
        q.push((self.vert_list[vertex], 0))
        seen[self.vert_list[vertex]] = 0

        while q:                # loop through the queue to get the vertex's neighbor
            curr = q.pop()          # curr is = (vertex, length)
            curr_vert = curr[0]     # curr_vert = vertex
            curr_length = curr[1]   # curr_length = length

            if curr_length > n:
                break

            for nei in curr_vert.get_neighbors():
                if nei not in seen:
                    if curr_length + 1 == n:        # this means the neighbor has met the right given length
                        path_nodes.append(self.vert_list[nei])

                    # increment the length in the dictionary, and enque the neighbor's value!!
                    new_pair = (self.vert_list[nei], curr_length + 1)
                    q.push(new_pair)

                    # add it to seen as well
                    seen[self.vert_list[nei]] = curr_length + 1

        return path_nodes


    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vert_list.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices())

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
