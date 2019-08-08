# CS-2.2-Labs

## Social Network Graph Tutorial
I will be using graph theory to solve a real world problem of finding connections - and recommending appropriate ones.  
The following project will be about building a graph of my nine closest friends and use graph theory to figure out interesting data about them!  

#### Learning outcomes
1. Implement a graph in code.
2. Use a variety of neighbor lookup algorithms for a given graph
3. Traverse a graph through various search methods

#### Graph representation of friends group

[image of graph]

#### Code implementation of the graph
[graph.py](https://github.com/SarinSwift/Graph-Tutorial/blob/master/Graph-Tutorial/graph.py)

The graph class:  
```
Graph()                              #creates a new, empty graph.
add_vertex(vert)                     #adds an instance of vertex to the graph.
add_edge(from_vert, to_vert)         #Adds a new, directed edge to the graph that connects two vertices.
add_edge(from_vert, to_vert, weight) #Adds a new, weighted, directed edge to the graph that connects two vertices.
get_vertex(vertKey)                  #finds the vertex in the graph named vertKey.
get_vertices()                       #returns the list of all vertices in the graph.
```

The vertex class:  
```
Vertex(vertex)                  #creates a new, vertex object with initialized id and it's neighbors.
add_neighbor(vertex, weight=0)  #adds a neighbor along a weighted edge.
get_neighbors()                 #returns the neighbors of this vertex
get_id()                        #returns the id of this vertex
get_edge_weight(vertex)         #returns the weight of this edge
```
