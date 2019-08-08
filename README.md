# CS-2.2-Labs

## Social Network Graph Tutorial
I will be using graph theory to solve a real world problem of finding connections - and recommending appropriate ones.  
The following project will be about building a graph of my nine closest friends and use graph theory to figure out interesting data about them!  

#### Learning outcomes
1. Implement a graph in code.
2. Use a variety of neighbor lookup algorithms for a given graph
3. Traverse a graph through various search methods

#### Graph representation of friends group

<img src="Image from iOS (8).jpg" width="350" height="280" />

#### Code implementation of the graph
[graph.py](https://github.com/SarinSwift/Graph-Tutorial/blob/master/Graph-Tutorial/graph.py)

Graph class:  
```
Graph()                              #creates a new, empty graph.
add_vertex(vert)                     #adds an instance of vertex to the graph.
add_edge(from_vert, to_vert)         #Adds a new, directed edge to the graph that connects two vertices.
add_edge(from_vert, to_vert, weight) #Adds a new, weighted, directed edge to the graph that connects two vertices.
get_vertex(vertKey)                  #finds the vertex in the graph named vertKey.
get_vertices()                       #returns the list of all vertices in the graph.
```

Vertex class:  
```
Vertex(vertex)                  #creates a new, vertex object with initialized id and it's neighbors.
add_neighbor(vertex, weight=0)  #adds a neighbor along a weighted edge.
get_neighbors()                 #returns the neighbors of this vertex
get_id()                        #returns the id of this vertex
get_edge_weight(vertex)         #returns the weight of this edge
```

##### Challenge 1
Implemented code for the graph class and vertex class to initialize our graph representation of our 9 friends! Running the file will output all the vertices in the graph and all the edges.  
ex.
```
The vertices are:  dict_keys(['Sarin', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
The edges are:
( Sarin , 1 )
( Sarin , 2 )
( Sarin , 3 )
 ...
```

##### Challenge 2
Complete code for the method get_neighbors() where it outputs all the nodes connected to the current node.  
Pseudocode:  
-Make sure the input node is actually in the graph  
-Find all edges for the input node  
-See what nodes are connected to the input node via the edge  
-Return the connected nodes  

##### Challenge 3
Breadth First Search (BFS)   
BFS - is an important searching algorithm to solve problems such as finding the shortest path in a graph. For example analyzing networks, mapping routes, and scheduling.  
What happens in BFS: We start from a vertex and follow its adjacent nodes.    
Implementation using queues.  
In this case, we can use bfs for finding all friends at a certain connection level away (friend's friend would be 2 connections from you)

<pre>
properties:  
    path of nodes array - to store all the current nodes that are n links away from given vertex
    seen dictionary - dictionary that looks like: [vertex: length]
    queue - which stores tuple object that look like: [(vertex, length)]

pseudocode:  
    start by adding given vertex to the q, and to the seen dictionary  
    loop through while the queue still has vertices  
    pop the item off q and store it in a variable called 'curr'  
        'curr' is a tuple of (vertex, length)  
        loop through neighbors of curr's vertex  
        if curr's length + 1 is the given length, we can append the neighbor! in to our path array   
            additionally, add this neighbor vertex and length + 1 to the queue, and the seen array   
    after finding all the neighbors that have a length of the given length, we can return the path array
</pre>


##### Challenge 4
Depth First Search (DFS)
DFS - An algorithm for traversing a graph. DFS traversals produces the minimum spanning tree and all pair of shortest path tree.  
Implementation using stacks.    
This challenge is to create a method `find_path(self, from_vert, to_vert)` and output the list of vertices that we pass to get from `from_vert` to `to_vert`  
This gives us a random path from the 2 vertices, but what if there was another path which was extremely shorter? We're going to optimize this in the next challenge


##### Challenge 5
Shortest Path Between 2 Vertices   
Here we are going to use a bfs solution, although dfs is also usable.  
There are 2 things that we will need to keep track of: the previous vertex, and the shortest ongoing next path.   
Write a method `find_shortest_path(self, src, dst)` that takes two vertices src(source) and dst(destination) as input, and outputs the list of vertices that make up the shortest path from src to dst.  
