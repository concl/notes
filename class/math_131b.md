
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

Define $P = \max (N, n_J)$, then consider $d(x_n, L$) for some $n \ge P$. We have $d(x_{n_P}, L) < \varepsilon$ and $d(x_n, x_{n_P}) < \varepsilon$, and by the triangle inequality we have $d(x_n, L) \le d(x_{n_P}, L)  + d(x_n, x_{n_P}) < 2 \varepsilon$.

If we take $\epsilon = 2\varepsilon$, this means we can construct for any $\epsilon > 0$ some $P \ge m$ such that $n \ge P$ implies that $d(x_n, L) < 2 \varepsilon = \epsilon$, which means $(x_n)_{n = m}^\infty$ must converge to $L$.

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




