# Week 1 Homework
## (Problem 2.2, the programming assignment is separate)

### Author: Carl Cortright
##### Date: 8/28/2016

Given an example adjacency matrix where a 1 represents a connection:

| vertexs | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 1 | 1 | 0 | 1 | 0 |
| 2 | 0 | 0 | 1 | 0 |
| 3 | 1 | 1 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 |

Algorithm:
1. Create a list of lists, where each list will contain a connected component. We will call this list **ConnectedComponents**

2. Create a map to store all of the vertexs that have already been visited. We will call this map **VisitedVertexes**

3. Starting at the first vertex, loop through all of the rows. If the vertex is not in **VisitedVertexes** add it to a new **ConnectedComponent** list. Add the **ConnectedComponent** to **ConnectedComponents**. Then, add the vertex to **VisitedVertexes**.

4. If in the previous step the vertex hadn't been visited yet, loop through all of the columns of that vertex. Add each edge found to the **ConnectedComponent** and recursively loop through all of it's columns doing the same.

5. Add each vertex visited to the **VisitedVertexes** list.

6. After all of the rows have been visited, **ConnectedComponents** will contain lists, where each list is a unique connected component. 


##### &copy; 2016 Carl Cortright All Rights Reserved
