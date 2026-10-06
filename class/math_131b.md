
## Definitions

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

**Ball**

Analogous to a ball in Euclidean space. Defined as the set of all points that are of distance less than $r$ from a center point.

$$
B_{(X, d)} (x_0, r) := \{x \in X : d(x, x_0) < r\}
$$
The ball can be abbreviated as $B(x_0, r)$ given context on which metric space we are using.


**Open Set**



**Closed Set**


**Interior**

**Exterior**

**Boundary**

**Adherrent**