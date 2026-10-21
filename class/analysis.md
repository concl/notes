
## Definitions

### Basics of Metric spaces
**Metric Space**

A set of objects (called points) together with a distance function, $d(x, y)$, that satisfies the following 4 axioms:

1. Distance between a point and itself is 0: $d(x,x) = 0$.
2. (Positivity): Distance between two **different** points is positive, $d(x,y) > 0$.
3. (Symmetry): The distance function is commutative, i.e. the order of the arguments doesn't matter: $d(x,y) = d(y, x)$.
4. (Triangle Inequality): The distance between 2 point, $a$ and $b$,  is less than or equal to the sum of the distance between $a$ and any third point $c$, and $b$ and $c$. 
$$
	\forall a, b, c \in X, d(a, b) \le d(a, c) + d(b, c)
$$

Metric spaces are often denoted as $(X, d)$, where $X$ is the set of points and $d$ is the metric. It's often inferable from context which metric a given set should be paired with, so we can abbreviate it as just $X$.

**Taxicab metric**

The $l^1$ norm, defined as:
$$
d_{l^1} (x,y) = |x_1 - y_1| + |x_2 - y_2| + \dots + |x_n - y_n|
$$
Related to the $l^2$ norm with the following inequality:

$$
d_{l^2} (x, y) \le d_{l^1} (x, y) \le \sqrt{n} \, d_{l^2} (x, y)
$$

**Sup norm metric**

Also known as the $l^\infty$ metric, measures the maximum difference in each component of the points.

$$d_{l^\infty} (x, y) = \sup \{ |x_i - y_i| : 1 \le i \le n \}$$

Related to the $l^2$ by the following:
$$
\frac{1}{\sqrt n}d_{l^2}(x, y) \le d_{l^\infty} (x, y) \le d_{l^2}(x, y)
$$

**Discrete metric**

Any set $X$ can be part of a metric space when defined with the discrete metric which is:
$$
d_{\text{disc}} (x, x) = 0
$$
$$
d_{\text{disc}} (x, y) = 1, \quad x \ne y
$$
In this space, every point is equally far apart.

**Convergence in a metric space**

Given a metric space $(X, d)$, and a sequence $(x^{n})_{n=m}^\infty$ , we say that the sequence converges to $x$ iff the limit $d(x^{(n)}, x)$ exists and is equal to $0$. 

In other words, for any $\varepsilon > 0$ there exists $N \ge m$ such that $d(x^{(n)}, x) < \varepsilon$ for all $n \ge N$ (we get this from expanding the definition of the limit of the sequence $d(x^{(n)}, x)$).



### Basic point set topology

**Ball**

Analogous to a ball in Euclidean space. Defined as the set of all points that are of distance less than $r$ from a center point.

$$
B_{(X, d)} (x_0, r) := \{x \in X : d(x, x_0) < r\}
$$
The ball can be abbreviated as $B(x_0, r)$ given context on which metric space we are using.


**Interior Point**

Let $E \subset X$ and $x_0 \in X$. $x_0$ is an interior point iff there exists $r > 0$ such that $B(x_0, r) \subseteq E$.

**Exterior Point**


Let $E \subset X$ and $x_0 \in X$. $x_0$ is an interior point iff there exists $r > 0$ such that $B(x_0, r) \cap E = \emptyset$.

**Boundary Point**

A point $x_0$ is a boundary point of $E$ iff it is neither an interior point or exterior point of $E$.

The set of all interior points, exterior points, and boundary points are called the interior, exterior, and boundary of E respectively. These are sometimes denoted as $\text{int} (E)$, $\text{ext}(E)$, or $\partial E$ respectively.

**Adherrent Point**

A point $x_0$ of $E$ is called an adherrent point of $E$ iff for any $r > 0$, $B(x_0, r)$ has a non empty intersection with $E$.

The set of all adherrent points is called the closure of $E$, denoted as $\overline E$.


**Open and Closed sets**

A set E is called open if it contains none of its boundary points. A set E is called closed if it contains all of its boundary points. Otherwise if the set contains some of its boundary points it is neither an open nor closed set.

It is possible for a set to be both open and closed if it has no boundary (for instance if $E = X$).

**Relative Topology**

Given a metric space $(X, d)$, a subset of the metric space $Y \subset X$ and a subset of the subset $E \subseteq Y$, we say that $E$ is *relatively open with respect to $Y$* iff it is open in the metric space $(Y, d|_{Y \times Y})$.  Similarly, $E$ is *relatively closed with respect to $Y$* iff it is closed in the metric space $(Y, d|_{Y \times Y})$.

A set $E$ is only relatively open with respect to $Y$ iff there exists an open subset $V$ of $X$ such that $E = V \cap Y$.

A set is only relatively closed with respect to $Y$ iff there exists a closed subset $K$ of $X$ such that $E = K \cap Y$.


**Limit Point**

For a sequence $(x_n)_{n=m}^\infty$ of points in a metric space $(X, d)$, and $L \in X$, we say $L$ is a limit point of $(x_n)_{n=m}^\infty$ iff for every $N > m$ and $\varepsilon > 0$ there exists $n > N$ where $d(L, x_n) \le \varepsilon$.

Equivalently $L$ is a limit point of the sequence if there exists some subsequence of the sequence that converges to $L$.


**Cauchy Sequence**

A sequence $(x_n)_{n=m}^\infty$ is **Cauchy** iff for any $\varepsilon > 0$ there exists $N \ge m$ such that for any $i, j \ge N$ we have $d(x_i, x_j) < \varepsilon$. 

Any convergent sequence is a Cauchy sequence, but not every Cauchy sequence converges. For instance, a sequence in $\mathbb Q$ with the standard metric that converges in $\mathbb R$ to some irrational number i.e. $\pi$ doesn't converge in $\mathbb Q$ since there doesn't exist any $L \in \mathbb Q$ which satisfies the limit definition.

However, if there exists some subsequence of a Cauchy sequence that converges, then the sequence must converge.

Proof: Suppose $(x_n)_{n=m}^\infty$ is Cauchy, and $(x_{n_j})_{j=1}^\infty$ converges to $L$. Then for any $\varepsilon > 0$ there exists $J \ge 1$ such that $j \ge J$ implies that $d(x_{n_j}, L) < \varepsilon$. For this same $\varepsilon$ there also exists $N \ge m$ such that for any $a, b \ge N$ we have $d(x_a, x_b) < \varepsilon$.

Define $P = \max (N, n_J)$, then consider $d(x_n, L$) for some $n \ge P$. Consider some $k$ such that $n_k \ge P$ (this implies that $k \ge J$, since subsequence indices are increasing, and thus $n_k \ge n_J \implies k \ge J$). We have $d(x_{n_k}, L) < \varepsilon$ and $d(x_n, x_{n_k}) < \varepsilon$, and by the triangle inequality we have $d(x_n, L) \le d(x_{n_k}, L)  + d(x_n, x_{n_k}) < 2 \varepsilon$.

Consider an arbitrary $\delta > 0$ and let $\varepsilon = \frac \delta 2$. Apply the previous argument, then we have $P$ such that $n \ge P$ implies that $d(x_n, L) < 2 \varepsilon = \delta$. Thus $(x_n)_{n = m}^\infty$ must converge to $L$.

**Complete Metric Spaces**

A metric space $(X, d)$ is called complete if every Cauchy sequence is convergent to a limit in $X$.

For instance, the metric space $(\mathbb R, d)$ is complete.

Complete metric spaces are "intrinsically closed" meaning that if they are a subspace, they are closed. For instance, if $Y \subset X$, and $(Y, d|_{Y \times Y})$ is complete, then $Y$ is closed in $(X, d)$. Conversely, if $(X, d)$ is complete, and $Y$ is a closed subset of $X$, then $(Y, d|_{Y \times Y})$ is complete.


**Compactness**

A metric space $(X, d)$ is called compact iff every sequence in $X$ has at least 1 subsequence that converges. A subset $Y$ of $X$ is called compact iff the subspace $(Y, d|_{Y \times Y})$ is compact.


**Bounded Set**

A subset $Y$ of the metric space $X$ is called bounded if there exists a ball $B(x_0, r)$ in $X$ that contains (supersets) $Y$. 


**Continuous Functions**

A function $f : X \to Y$, where $(X, d_X)$ and $(Y, d_Y)$ are metric spaces is continuous at a point $x_0 \in X$ iff for any $\varepsilon > 0$ there exists $\delta > 0$ such that for any $x \in X$ where $d_X(x, x_0) < \delta$ implies that $d_Y(f(x), f(x_0)) < \varepsilon$. 

This is equivalent to saying that for any sequence $(x_n)_{n = m}^\infty$ in $X$ that converges to $x_0$ with respect to the metric $d_X$, we have that $f(x_n)$ converges to $f(x_0) \in Y$ with respect to the metric $d_Y$.


**Uniform Continuity**

A function $f: X \to Y$ is called uniformly continuous if for any $\varepsilon > 0$ there exists $\delta > 0$ such that if there are two points $x, x' \in X$ such that $d(x, x') < \delta$ then $d(f(x), f(x')) < \varepsilon$. 

In other words, for any given $\varepsilon >0$ there is a distance which forces points that are closer than that distance to cause deviations in the function value that are less than $\varepsilon$. This differs from ordinary continuity in that the same $\delta$ has to work for every point in $X$ (for ordinary continuity, the choice of $\delta$ can depend on both $x$ and $\varepsilon$ instead of only $\varepsilon$).

A function that is continuous on a compact set $X$ is uniformly continuous (and the converse is trivially true).

## Theorems and Properties

**Basic properties of open and closed sets**

1. A subset $E$ is open iff $E = \text{int} (E)$
2. If $E$ is closed then the limit $x$ of any sequence contained in $E$ is a part of $E$. 
3. The ball $B(x_0, r) = \{ x \in X : d(x_0, x) < r \}$ is an open set.
4. Any singleton set consisting of only 1 element $x_0 \in X$ is closed.
5. A subset $E \subset X$ is open iff $X \setminus E$ is closed.
6. The **intersection** of a finite collection of open sets is open. The **union** of a finite collection of closed sets is closed.
7. The **union** of a finite, countably infinite, or uncountably infinite collection of open sets is open. The **intersection** of a finite, countably infinite, or uncountably infinite collection of closed sets is closed.
8. The interior of a set $E$ is the largest open set that is contained in $E$, i.e. if an open set $V \subseteq E$ then $V \subseteq \text{int}(E)$. The closure of a set $E$ is the smallest closed set that contains $E$, i.e. if any other closed set $K \supset E$ then $K \supset \overline E$. 

**Heine-Borel Theorem (Closed and Bounded Subsets with $l^n$ norms are compact)**

If $(R^n, d)$ is a Euclidean space with either the Euclidean, taxicab, or sup norm metric, then a subset $E$ of $R^n$ is compact iff it is closed and bounded.

HB is not true for general metric spaces, for instance $(\mathbb Z, d_{\text{disc}})$ is closed and bounded (since the ball $B(0, 2)$ encompasses the entire space, and $\mathbb Z$ contains all of its boundary points where $\partial \mathbb Z = \emptyset$). However we can take the sequence $1, 2, 3, \dots$ which has no convergent subsequence.

**(Infinite) Open Covers of Compact Sets Must Have Finite Subcovers**

Let $(X, d)$ be a metric space, and let $Y$ be a compact subset of $X$. Let $(V_\alpha)_{\alpha \in I}$ be a collection of open sets in $X$, and suppose that:
$$Y \subseteq \bigcup_{\alpha \in I} V_\alpha$$
($Y$ is covered by the union of the collection of open sets $(V_\alpha)_{\alpha \in I}$, an open cover).

Then there is a finite subset $F \subseteq I$ such that:
$$Y \subseteq \bigcup_{\alpha \in F} V_\alpha$$
($Y$ is covered by a finite subset of the collection of open sets).

This notion has a converse, where if every open cover of a set $Y$ has a finite subcover, then $Y$ is compact.

For metric spaces, this definition is equivalent to the sequence definition of compact sets, but in general topological spaces this definition is slightly different and more "fundamental".


**Maximum Principle**

A continuous function $f : X \to \mathbb R$, where $(X, d)$ is a compact metric space, is bounded (the image is a bounded subset of $\mathbb R$). Furthermore, $f$ attains it maximum value at some point $x_\max \in X$ and its minimum value at some point $x_\min \in X$.

