

## Definitions


**Complete Graph**
The complete graph on $n$ vertices is denoted $K_n$ and consists of $n$ vertices where there is an edge between every pair of vertices.


**Complete Bipartite Graph**
The complete bipartite graph between 2 sets of vertices with sizes $n, m$ is denoted $K_{n, m}$, which contains $n + m$ vertices that are split into 2 groups with sizes $n$ and $m$. There is an edge between every pair of vertices between the 2 groups.


**Subgraph**
A graph $G$ is a subgraph of $G'$ iff its vertex and edge sets are subsets of $G'$.

A subgraph $G$ of $G'$ is called an induced subgraph iff its vertex set is a subset but its edge set consists of all edges in $G'$ that are between vertices in $V(G)$. 


**Path**
Subgraph of G isomorphic to $P_t$  is called a path in G.

$P_t = (v_0, v_1, \dots, v_t)$ or $(e_1, e_2, \dots, e_t)$.

with $e_i = (v_{i - 1}, v_i)$.

The length of a path is the number of edges in the path.


**Cycle**
subgraph of G isomorphic to $C_t, t\ge 3$
$(v_0, v_1, \dots, v_{t - 1}, v_0)$ 

The cycle on $n$ vertices is denoted $C_n$ and is defined as:
$$
V = \{1, 2, \dots, n\}, \quad E = \{\{i, i + 1\} : i \in [1, n - 1]\} \cup \{\{1, n\}\}
$$


**Walk**
A sequence of vertices is called a walk if every pair of adjacent vertices has an edge between them


**Complement**
The complement of $G$, $\bar G$ or $G^c$, is on the same set of vertices, where there is an edge iff two vertices don't have an edge in the original graph.


**Connectedness**
We say a graph $G$ is connected if any pair of vertices in $G$ have a path a path between them.


**Equivalence relation**
$v$ ~ $w$ if there is a walk between the 2 vertices. This is an equivalence relation (we assume $v$ ~ $v$), and the equivalence classes of ~ are called a connected components.


**Distances** 
The distance between 2 vertices is the minimum of the lengths of all paths between the 2 vertices.


**Score sequence / Degree sequence**
The score sequence of a graph is one of (oftentimes) many sequences of a graph, where an order of vertices is chosen, and the degrees of those nodes are listed out.


**Graph Isomorphism**
Two graphs, $G$ and $G'$ are called **equal** if their sets of vertices and edges are the same. Two graphs are called **isomorphic** if there exists a bijective function that maps vertices from $G$ to $G'$ while preserving the edge relationships (the graphs have the same "structure"). Formally they are isomorphic iff there exists a bijection $f: V \to V'$ such that:

$$
\{x, y\} \in E \iff \{f(x), f(y)\} \in E'
$$

where $x \ne y$

We denote an isomorphism with $G \cong G'$

**Jordan Curve**
A closed curve without intersections. We can define this as a mapping $f$ from $[0, 1]$ to the plane where it is injective except for $f(0) = f(1)$.


**Combinatorial Characterization of Planar Graph**
A graph is planar iff every subdivision of the graph is planar.

## Theorems

**Handshake Lemma**
The number of odd degree nodes in a graph is even. More precisely the sum of degrees of the nodes is $2|E|$.


**Score Theorem / Havel Hakimi**
Let $D = (d_1, d_2, \dots, d_n)$ be a sequence of natural numbers with $n > 1$, and suppose the sequence is non decreasing. Define $D'$ as a sequence $(d'_1, d'_2, \dots, d'_{n -1})$  where:
$$
	d'_i = 
	\begin{cases}
		d_i & \text{if } i < n - d_n \\
		d_i - 1  & \text{if } i \ge n - d_n \\
	\end{cases}	
$$

Then $D$ is a valid degree sequence iff $D'$ is a valid degree sequence.

Informal Justification:

We can show the reverse implication $D'$ valid $\implies$ $D$ valid easily. Informally, we can take the graph that $D'$ represents, take the $d_n$ nodes that the last $d_n$ scores in $D'$ represent, and draw an edge between these nodes and a new node, which will have a degree of $d_n$.

Now for the forward implication. Suppose $D$ was valid. Then consider the set of all possible graphs that has a score sequence of $D$. We claim that there exists a graph that consists of the node with degree $d_n$ being connected to the $d_n$ nodes that are represented by the last $d_n$ elements of $D$ (excluding the node with $d_n$ itself).

Now we show this claim is true informally. Take some arbitrary graph with score sequence $D$. Consider a node with score $d_n$, and let this node represent the last element in $D$. We can construct the graph in the claim by drawing an edge between this node and every node represented by the last $d_n$ elements in $D$, removing the edges between this node and every node outside of the last $d_n$ elements in $D$ and pairing up nodes from these 2 groups and drawing edges between them. 

Based on this theorem, we can devise an algorithm for showing that a score sequence is valid or invalid, and construct a graph with a given valid score sequence. We start with the node with the largest degree, materialize it by drawing an edge between this node and the next $d_n$ nodes, rearrange the nodes in $D'$, and repeat the process until we reach a score sequence that is clearly impossible or possible.


**Cayley's Formula**
The number of minimum spanning trees in $K_n$ is $n^{n - 2}$.

**Jordan Curve Theorem**
Any Jordan curve $k$ divides the plane into exactly 2 connected parts, called the interior and exterior. We can define an equivalence relation on the set $\mathbb R^2 / k$ (the plane without the boundary) by setting $x \approx y$ if they can be connected with an arc that doesn't intersect $k$. This equivalence relation will have 2 classes, where one is unbounded and the other is bounded.

**$K_5$ is not planar**
Informal Justification: Suppose FSOC there existed a planar drawing of $K_5$, and let $b_1, b_2, \dots b_5$ be the points corresponding to each vertex in an arbitrary planar drawing of $K_5$. Let $\alpha(i, j)$ be the arc connecting the points $b_i$ and $b_j$. 

Since the vertices $b_1, b_2, b_3$ form a cycle in $K_5$, the edges $\alpha(1, 2), \alpha(2,3), \alpha(3, 1)$ form a Jordan curve in the plane. We must have that either both $b_4$ and $b_5$ are in the interior of this curve, or both are in the exterior, otherwise $\alpha(4, 5)$ would intersect with this curve.

Consider the case where $b_4$ lies on the interior of the curve, and thus $b_5$ must also lie on the interior of this curve. Since there are cycles that form between 2 of the vertices from 1 to 3 and vertex 4, there are 3 regions inside the curve formed by 1, 2, and 3, (we assume with a little bit of intuition that these 3 regions form the interior of the original curve) and having $b_5$ in each of these regions necessitates an intersection between the boundary of that region and the missing vertex that is on the exterior of that region.

A similar argument shows that it is also impossible for both $b_4$ and $b_5$ to be on the exterior of the original curve, and thus $K_5$ is not planar.


**Cycles in planar 2 connected graphs**
If $G$ is a 2-connected planar graph, then every face in any planar drawing of $G$ is a region (interior or exterior) of some cycle in $G$. (For brevity, we call the Jordan curve formed by taking the edges in a cycle in a planar drawing of a 2-connected graph a cycle too).


**Kuratowski Theorem**
A graph $G$ is planar iff it has no subgraph isomorphic to a subdivision of $K_{3, 3}$ or to a subdivision of $K_5$.


