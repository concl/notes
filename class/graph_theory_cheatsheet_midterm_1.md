# Graph Theory Cheatsheet

---

## 1. Basic Graph Terminology

### Formal Definitions
* **Graph:** An ordered pair $G = (V, E)$, where:
  * $V$ (or $V(G)$) is a non-empty set of **vertices** (or nodes).
  * $E$ (or $E(G)$) is a set of **edges**, where each $e \in E$ is an unordered pair $\{u, v\}$ of distinct vertices from $V$ (for simple undirected graphs). We write $uv$ or $vu$ as shorthand.
  * The **order** of $G$ is $|V| = n$; the **size** of $G$ is $|E| = m$.
* **Adjacency & Incidence:** Vertices $u$ and $v$ are **adjacent** (neighbors, $u \sim v$) if $uv \in E$. The edge $e = uv$ is **incident** to $u$ and $v$.

### Sequences of Vertices and Edges
Let $G = (V, E)$ be a graph.
* **Walk:** An alternating sequence of vertices and edges:
  $$W = (v_0, e_1, v_1, e_2, \dots, e_k, v_k)$$
  where $e_i = v_{i-1}v_i \in E$ for all $1 \le i \le k$. The **length** of $W$ is the number of edges, $k$. A walk is **closed** if $v_0 = v_k$.
* **Trail:** A walk in which all edges are distinct ($e_i \neq e_j$ for $i \neq j$).
* **Path:** A walk in which all vertices (and consequently all edges) are distinct.
  * A $u$-$v$ path of length $k$ is denoted $P_{k+1}$ (having $k+1$ vertices and $k$ edges).
  * **Proposition:** Every $u$-$v$ walk contains a $u$-$v$ path as a subsequence.
* **Cycle:** A closed walk $(v_0, v_1, \dots, v_k, v_0)$ of length $k \ge 3$ where $v_0, v_1, \dots, v_{k-1}$ are distinct. Denoted $C_k$.
  * **Girth:** $\mathrm{girth}(G)$ is the length of a shortest cycle in $G$ (defined as $\infty$ if $G$ is acyclic).

### Subgraphs
* **Subgraph:** $H = (V', E')$ is a subgraph of $G = (V, E)$ ($H \subseteq G$) if $V' \subseteq V$ and $E' \subseteq E$ with the endpoint condition that $uv \in E' \implies u, v \in V'$.
* **Spanning Subgraph:** A subgraph $H \subseteq G$ where $V(H) = V(G)$.
* **Induced Subgraph:** For $S \subseteq V$, the subgraph induced by $S$, denoted $G[S]$, has vertex set $S$ and edge set:
  $$E(G[S]) = \{uv \in E(G) : u, v \in S\}$$

### Connectivity & Components
* **Connected Vertices:** Vertices $u, v \in V$ are connected if there exists a $u$-$v$ path in $G$.
* **Equivalence Relation:** Connectivity is an equivalence relation on $V$:
  * Reflexive: $u$ is connected to $u$ (path of length $0$).
  * Symmetric: $u \leftrightarrow v \implies v \leftrightarrow u$.
  * Transitive: $u \leftrightarrow v \land v \leftrightarrow w \implies u \leftrightarrow w$.
* **Connected Component:** An equivalence class of $V$ under the connectivity relation, or a maximal connected subgraph of $G$.
* **Connected Graph:** A graph with exactly $1$ connected component.

---

## 2. Isomorphism, Counting Labeled Graphs, and Automorphisms

### Graph Isomorphism
* **Definition:** Graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are **isomorphic** ($G_1 \cong G_2$) if there exists a bijection $f: V_1 \to V_2$ such that:
  $$uv \in E_1 \iff f(u)f(v) \in E_2 \quad \forall u, v \in V_1$$
* **Isomorphism Invariants:** Properties preserved under isomorphism:
  * Number of vertices $|V|$ and edges $|E|$.
  * Degree sequence.
  * Number of connected components.
  * Subgraph counts (e.g., number of triangles $K_3$, cycles of length $k$).
  * Spectrum of the adjacency matrix.

### Automorphisms
* **Definition:** An **automorphism** of $G$ is an isomorphism from $G$ to itself ($f: V \to V$).
* **Automorphism Group:** The set of all automorphisms forms a group under function composition, denoted $\mathrm{Aut}(G) \le \mathrm{Sym}(V) \cong S_n$.
* **Examples:**
  * Complete graph: $\mathrm{Aut}(K_n) \cong S_n$, with order $|\mathrm{Aut}(K_n)| = n!$.
  * Empty graph: $\mathrm{Aut}(\overline{K_n}) \cong S_n$.
  * Cycle: $\mathrm{Aut}(C_n) \cong D_{2n}$ (dihedral group of order $2n$, for $n \ge 3$).
  * Path: $\mathrm{Aut}(P_n) \cong \mathbb{Z}_2$ for $n \ge 2$.
  * Asymmetric graph: A graph where $|\mathrm{Aut}(G)| = 1$ (the only automorphism is the identity).

### Counting Labeled Graphs
* **Total Labeled Graphs on $n$ vertices:**
  * For a fixed vertex set $V = \{1, 2, \dots, n\}$, there are $\binom{n}{2} = \frac{n(n-1)}{2}$ potential edges.
  * Each edge can independently be present or absent.
  * Total number of distinct labeled simple graphs:
    $$2^{\binom{n}{2}}$$
* **Orbit-Stabilizer Connection:**
  * The symmetric group $S_n$ acts on the set of labeled graphs $\mathcal{G}_n$ by relabeling.
  * The orbit of a graph $G$ corresponds to all labeled graphs isomorphic to $G$.
  * By the Orbit-Stabilizer Theorem:
    $$|\mathrm{Orbit}(G)| = \frac{|S_n|}{|\mathrm{Stab}_{S_n}(G)|} = \frac{n!}{|\mathrm{Aut}(G)|}$$
  * Therefore, the number of distinct labeled graphs isomorphic to an unlabeled graph $G$ is $\frac{n!}{|\mathrm{Aut}(G)|}$.

---

## 3. Degrees, Handshaking Lemma, and Havel–Hakimi

### Vertex Degree
* **Degree:** For $v \in V$, $\deg(v) = d(v) = |N(v)|$, the number of edges incident to $v$.
* **Extrema & Average:**
  * Minimum degree: $\delta(G) = \min_{v \in V} \deg(v)$.
  * Maximum degree: $\Delta(G) = \max_{v \in V} \deg(v)$.
  * Average degree: $\bar{d}(G) = \frac{1}{|V|} \sum_{v \in V} \deg(v) = \frac{2|E|}{|V|}$.
* **Regular Graph:** A graph is $k$-regular if $\deg(v) = k$ for all $v \in V$.

### The Handshaking Lemma
* **Theorem:** For any undirected graph $G = (V, E)$:
  $$\sum_{v \in V} \deg(v) = 2|E|$$
  * *Proof sketch:* Each edge $e = uv$ contributes $1$ to $\deg(u)$ and $1$ to $\deg(v)$, thus contributing exactly $2$ to the sum of degrees.
* **Corollary:** In every graph, the number of vertices with odd degree is **even**.

### Degree Sequences & Graphic Sequences
* **Degree Sequence:** A monotonic sequence of non-negative integers representing the vertex degrees:
  $$d_1 \ge d_2 \ge \dots \ge d_n$$
* **Graphic Sequence:** A sequence $(d_1, \dots, d_n)$ of non-negative integers is called **graphic** if there exists a simple graph $G$ whose degree sequence is precisely $(d_1, \dots, d_n)$.

### The Havel–Hakimi Theorem
* **Theorem (Havel 1955, Hakimi 1962):**
  A sequence $D = (d_1, d_2, \dots, d_n)$ with $n-1 \ge d_1 \ge d_2 \ge \dots \ge d_n \ge 0$ is graphic if and only if the reduced sequence
  $$D' = (d_2 - 1, \; d_3 - 1, \; \dots, \; d_{d_1 + 1} - 1, \; d_{d_1 + 2}, \; \dots, \; d_n)$$
  is graphic (after sorting in non-increasing order).

* **Algorithm to Test if a Sequence is Graphic:**
  1. If any element is $< 0$ or $d_1 \ge n$, **output FALSE**.
  2. If all elements are $0$, **output TRUE**.
  3. Sort the sequence descending: $d_1 \ge d_2 \ge \dots \ge d_n$.
  4. Remove $d_1$, and subtract $1$ from each of the next $d_1$ elements: $d_2, \dots, d_{d_1 + 1}$.
  5. Re-sort the resulting list descending and repeat from step 1.

---

## 4. Eulerian Tours and Characterization

### Definitions
* **Eulerian Trail:** A trail that visits every edge of $G$ exactly once.
* **Eulerian Tour (or Circuit):** A closed walk (trail) that traverses every edge of $G$ exactly once and returns to the starting vertex.
* **Eulerian Graph:** A graph that admits an Eulerian tour.

### Characterization Theorems
* **Euler's Theorem (Closed Tours):**
  A connected graph $G$ has an Eulerian tour if and only if every vertex has an **even degree**:
  $$\deg(v) \equiv 0 \pmod 2 \quad \forall v \in V$$
  *(Note: Isolated vertices with $\deg(v) = 0$ are ignored in the connectivity requirement).*

* **Open Trails (Eulerian Paths):**
  A connected graph $G$ has an open Eulerian trail (starts at $u$ and ends at $v \neq u$) if and only if exactly **two** vertices have odd degree (these two vertices are $u$ and $v$).

### Algorithmic Approaches
* **Hierholzer’s Algorithm ($O(|E|)$ time):**
  1. Start at any vertex $v$ (or an odd vertex if finding an open trail).
  2. Follow an arbitrary path of unused edges until returning to the start vertex (a closed sub-tour).
  3. While there exist vertices on the current tour with unused incident edges:
     * Select a vertex $w$ on the current tour with an unused edge.
     * Follow a new closed sub-tour from $w$ through unused edges.
     * Splice this sub-tour into the original tour at $w$.
  4. Output the complete cycle.
* **Fleury’s Algorithm ($O(|E|^2)$ naive):**
  * Traverse edges one by one, deleting each traversed edge.
  * Rule: Never cross a **bridge** (cut-edge) of the remaining graph unless there is no alternative.

---

## 5. 2-Connected Graphs, Common-Cycle, and Ear Decompositions

### Cuts and Connectivity
* **Cut-Vertex (Articulation Point):** A vertex $v \in V$ such that the number of connected components of $G - v$ is strictly greater than that of $G$.
* **Bridge (Cut-Edge):** An edge $e \in E$ such that $G - e$ has more connected components than $G$.
* **$k$-Connected Graph:**
  * A graph $G$ is **$k$-vertex-connected** (or $k$-connected) if $|V| \ge k+1$ and the removal of any subset of fewer than $k$ vertices leaves a connected graph.
  * The **connectivity** $\kappa(G)$ is the maximum $k$ such that $G$ is $k$-connected.
* **2-Connected Graph:**
  * $|V| \ge 3$, connected, and contains **no cut-vertices** ($\kappa(G) \ge 2$).

### Common-Cycle Characterization (Whitney's 2-Connected Theorem)
* **Theorem:** For a graph $G$ with $|V| \ge 3$, the following statements are equivalent:
  1. $G$ is 2-connected (connected and has no cut-vertices).
  2. Any two vertices $u, v \in V$ lie on a **common simple cycle**.
  3. Any vertex and any edge lie on a common simple cycle.
  4. Any two edges $e_1, e_2 \in E$ lie on a common simple cycle (provided no isolated vertices exist).
  5. For any pair of vertices $u, v$ and any edge $e$, there exists a path between $u$ and $v$ containing $e$.
* **Menger's Theorem ($k=2$ special case):**
  A graph $G$ is 2-connected if and only if between every pair of distinct vertices $u$ and $v$, there exist at least **two internally disjoint paths**.

### Ear Decompositions
* **Ear:** Given a subgraph $H \subseteq G$, an **ear** of $H$ in $G$ is a non-trivial path $P = (v_0, v_1, \dots, v_k)$ in $G$ such that:
  * Its endpoints $v_0, v_k \in V(H)$.
  * Its internal vertices $v_1, \dots, v_{k-1} \notin V(H)$.
  * The edges of $P$ do not belong to $H$.
  * If $v_0 = v_k$, $P$ is a closed ear (a cycle meeting $H$ at a single vertex). An ear is an **open ear** if $v_0 \neq v_k$.

* **Ear Decomposition:**
  A decomposition of $G$ into a sequence of subgraphs:
  $$G_0 \subset G_1 \subset G_2 \subset \dots \subset G_m = G$$
  where:
  1. $G_0$ is a simple cycle $C$.
  2. Each $G_i$ ($1 \le i \le m$) is obtained from $G_{i-1}$ by adding an ear $P_i$:
     $$G_i = G_{i-1} \cup P_i$$
* **Open Ear Decomposition:** An ear decomposition where every ear $P_i$ ($i \ge 1$) is an **open ear** ($v_0 \neq v_k$).

### The Ear Decomposition Theorem (Whitney 1932)
* **Theorem:**
  * A graph $G$ is **2-connected** if and only if it admits an **open ear decomposition**.
  * A graph $G$ is **2-edge-connected** (bridgeless) if and only if it admits an **ear decomposition** (where closed ears are permitted).