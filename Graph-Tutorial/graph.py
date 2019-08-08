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
        seen = dict()           # dictionary of vertex and length that has been visited
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

    def find_path(self, from_vert, to_vert, visited=None):
        '''
        returns a path from a given vertex to another given vertex. This will not give us the shortest path,
        but rather just a random path that got chosen.
        '''
        # Make sure that both nodes from_vert and to_vert are actually in the graph
        if from_vert not in self.vert_list.keys() or to_vert not in self.vert_list.keys():
            print("No available vertices in this graph!")
            return

        # initializing the visited array for the first iteration
        if visited == None:
            visited = []

        visited.append(from_vert)
        # return true so we know that we've hit the end!! And this is where we're going to check
        # the bool when we're updating the recursion call parameters down below.
        if from_vert == to_vert:
            return True

        # loop through the neighbors of our current vertex and call make the recursion call with the neighbor vertex
        for neighbor in from_vert.neighbors:
            if neighbor not in visited:
                if find_path(neighbor, to_vert, visited) == True:
                    return visited

        # No path within these vertices
        return None

    def find_shortest_path(self, src, dst):
        '''
        Returns the shortest path from a given vertex to another given vertex. This is an optimization from
        the method above. We're adding a new property to our Vertex class named parent because we're breaking
        down the graph into a tree looking form. And we return the shortest path by going up the tree!
        '''
        q = queue.Queue()       # where we perform bfs
        seen = set()            # keeps track of seen vertices
        path = []               # the path of vertices from from_vert to to_vert

        # add to the queue
        q.put(src)

        while q:
            curr = q.get()
            seen.add(curr)

            if curr == dst:
                break

            for neighbor in curr.neighbors:
                if neighbor not in seen:
                    q.put(neighbor)
                    neighbor.parent = curr
                if neighbor == dst:
                    break

        # loop so we can go up the tree from when we set the parents
        node = dst
        while node:
            path.append(node.id)
            node = node.parent

        # after creting the path from the last up, we should return in reverse order so it
        # goes from src to dst
        return path[::-1]




    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vert_list.values())


if __name__ == "__main__":

    # Create the graph
    g = Graph()

    # Add friends (including myself)
    g.add_vertex("Sarin")
    g.add_vertex("AAA")
    g.add_vertex("BBB")
    g.add_vertex("CCC")
    g.add_vertex("DDD")
    g.add_vertex("EEE")
    g.add_vertex("FFF")
    g.add_vertex("GGG")
    g.add_vertex("HHH")
    g.add_vertex("III")

    # Add connections (non weighted edges for now)
    g.add_edge("Sarin", "AAA")
    g.add_edge("Sarin", "BBB")
    g.add_edge("Sarin", "CCC")
    g.add_edge("Sarin", "DDD")
    g.add_edge("Sarin", "EEE")
    g.add_edge("Sarin", "FFF")
    g.add_edge("Sarin", "GGG")
    g.add_edge("Sarin", "HHH")
    g.add_edge("Sarin", "III")

    # All connections of my friend AAA:
    g.add_edge("AAA", "III")
    g.add_edge("AAA", "HHH")
    g.add_edge("AAA", "FFF")

    # All connections of my friend BBB:
    g.add_edge("BBB", "CCC")

    # All connections of my friend CCC:
    g.add_edge("CCC", "BBB")

    # All connections of my friend DDD:
    g.add_edge("DDD", "III")

    # All connections of my friend EEE:
    g.add_edge("EEE", "FFF")

    # All connections of my friend FFF:
    g.add_edge("FFF", "EEE")
    g.add_edge("FFF", "AAA")
    g.add_edge("FFF", "GGG")

    # All connections of my friend GGG:
    g.add_edge("GGG", "FFF")

    # All connections of my friend HHH:
    g.add_edge("HHH", "AAA")

    # All connections of my friend III:
    g.add_edge("III", "AAA")
    g.add_edge("III", "DDD")

    print("finding path")
    print(g.find_path(g.vert_list["Sarin"], g.vert_list["AAA"]))

    # Output the vertices & edges
    # vertices:
    print("The vertices are: ", g.get_vertices())

    # edges:
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
