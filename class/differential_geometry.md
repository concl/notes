
## Definitions

**Curve**

A curve is a function $\alpha : I \to  \mathbb R^3$ that takes a real number from an interval and maps it to a point. Most of the time we deal with differentiable curves. Thus we can define a curve as:
$$
\alpha(t) = (x(t), y(t), z(t))
$$
where $x, y, z$ are differentiable.

**Trace**

The trace of a curve is its image. Thus for $\alpha : I \to  \mathbb R^3$, the trace is $\alpha(I) = \{ p \in \mathbb R^3 : p = \alpha(t) \}$.

**Regular**

A curve $\alpha(t$) that is **regular** is a curve that has $\alpha'(t) \ne \mathbf 0$ for all $t$ in its domain. On a regular point $\alpha(t_0)$ (a point that is not singular), the tangent line is defined to be:
$$
\{ \alpha(t_0) + \lambda \alpha'(t_0) : \lambda \in \mathbb R\}
$$


**Singular**

A point on a curve $\alpha(t)$ is singular if $\alpha'(t) = 0$.



**Reparametrization**

if $h: J \to I$ is a diffeomorphism (bijective and has both it and its inverse differentiable, equivalently that $h'(t) \ne 0$, and $h(J) = I$).

Then we have $\beta (t) = \alpha \circ h (t) : J \to \mathbb R^3$, which is a reparametrization of $\alpha$, and:
$$
\beta'(t) = h'(t) \alpha'(h(t))
$$
This means that the trace and regularity are both unchanged, and same with the tangent line at the corresponding points.




**Frenet-Serret Frame**

The tangent, normal, and binormal vectors to a curve (parametrized by arc length):
$$
T(s) = \frac{dr}{ds}
$$
$$
N(s) = \frac{T'(s)}{||T'(s)||}
$$
$$
B(s) = T(s) \times N(s)
$$

**Frenet-Serret formulas**

$$
\frac{dT}{ds} = \kappa N
$$

$$
\frac{dN}{ds} = -\kappa T -\tau B
$$
$$
\frac{dB}{ds} = \tau N
$$
($\kappa$ = curvature of the curve, $\tau$ is torsion)

We can alternatively write this as:
$$
\begin{bmatrix}
\frac{dT}{ds} \\
\frac{dN}{ds} \\
\frac{dB}{ds} \\
\end{bmatrix}
=
\begin{bmatrix}
0 & \kappa & 0 \\
-\kappa & 0 & -\tau \\
0 & \tau & 0
\end{bmatrix}
\begin{bmatrix}
T \\
N \\
B \\
\end{bmatrix}
$$


**Curvature and Torsion**

We can calculate the curvature of a curve at any given point (if the curve is parametrized by arc length) with:

$$
k = |\alpha''(s)|
$$

We can calculate the torsion with its definition in the Frenet-Serret formulas.

**Osculating Plane**

The osculating plane is the plane where a curve is "locally embedded" in 3D space: the tangent and normal vectors span this plane. The binormal vector is orthogonal to this plane.



**Differentials (i.e. $d F_p (v)$)

The standard way to write the "derivative" of a map $f: R^{n} \to R^m$ is $D f(x)$ (which is an $m \times n$ matrix, since it maps n dimensional column vectors to m dimensional column vectors). In differential geometry, this can be written as $d F_x$. Since this is a matrix representing the local linear transformation close to $x$ of that point, we apply it to a vector like $d F_x(v)$.

**Chain Rule**

$$D (G \circ F) (x) = D G(F(x)) D F(x)$$

Equivalently with differentials:

$$
d(G \circ F)_x = DG(F(x))DF(x)
$$


**Homeomorphism (Topological equivalence)**

A function $f: X \to Y$ is called a Homeomorphism if:
1. Bijective: It is injective and surjective
2. Continuous: No sudden jumps or breaks
3. Continuous inverse: The inverse is continuous

A Homeomorphism can be thought of as a "rubber sheet deformation" between 1 shape and another. There exists a homeomorphism between a coffee mug and a donut.

**Diffeomorphism**

A function $f: X \to Y$ is a Diffeomorphism if:
1. Bijective
2. Smooth: It is infinitely differentiable everywhere
3. Smooth Inverse

**Regular Surface**

A subset $S \subset R^3$ is a regular surface if every $p \in S$ has a relatively open neighborhood $V \subset S$ and a map $x : U \to V, U \subset R^2$ open such that 

1. $x$ is smooth
2. $x$ is a homeomorphism onto $V$
3. $dx_p$ has rank 2 for every $p \in U$

$x$ is then called a coordinate patch.

We can make sure that $dx_p$ is rank 2 by ensuring that the columns are linearly independent.

## Notes

**Torsion Properties**
- If $\tau = 0$ uniformly over a curve, then the curve is planar

**Arc Length Parametrization**
- For a curve $\alpha(s)$ parametrized by arc length, we have that $T(s) = \alpha'(s)$. Thus, if we know $T(s)$ we can integrate it to get $\alpha(s)$.

**Parametrizing a curve given implicitly**

Use some trig or hyperbolic identity. Examples:
- $x^2/a^2 + y^2/b^2 = 1$: Parametrized by $(a \cos t, b \sin t), t\in [0, 2\pi)$.
- $x^2/a^2 - y^2/b^2 = 1$: Parametrized by $(a \cosh t, b \sinh t), t\in \mathbb R$ (right branch only) or $(a \sec t, b \tan t), t \neq \frac \pi 2$ (both branches).
- $y^2 = x^2 - x^4$: We can get $y = x \sqrt{1 - x^2}$ for $|x| \le 1$, and a parametrization is $(\sin t, \sin t \cos t)$.
- $y = f(x)$: We can get $(t, f(t))$.

State the domain and whether the parametrization is injective.

**Spheres**

If a curve $\alpha (t)$ has the property $\langle \alpha(t), \alpha'(t)\rangle = 0$ for all $t$ in the domain, then $|\alpha(t)|$ must be constant. Thus the trace is part of a sphere centered at the origin.

If a curve $\alpha (t)$ has the property $\langle \alpha(t) - a, \alpha'(t)\rangle = 0$ for all $t$ in the domain, then $|\alpha(t) - a|$ is constant, so the trace is part of a sphere centered at $a$.

**Maximal and minimal points of a curve**

If $|\alpha (t_0)|$ is maximal or minimal over the trace, then $\langle \alpha(t_0), \alpha'(t_0) \rangle = 0$.

**Constant angles**

If the angle $\theta$ between $\alpha$ and $\alpha'$ is constant, then we have that:
$$
\cos \theta = \frac{\langle \alpha, \alpha'\rangle}{|\alpha| | \alpha'|}
$$
is constant.

**Tools**
- (In the x-y plane) Let $\theta(s)$ be the angle that the tangent of a curve makes with the x-axis. Then we have: $T(s) = \left(\cos (\theta(s)), \sin (\theta(s))\right)$. Thus, $T'(s) = \theta'(s) \left(-\sin (\theta(s)), \cos (\theta(s))\right)$. And by the Frenet-Serret formula we have $\theta'(s) = \kappa(s)$. 
	- This is useful, because if we know $\kappa(s)$ then we can integrate it to get $\theta(s)$, which gives us an expression for $T(s)$.


**Inverse Function Theorem**

If $F: U \subset R^n \to R^n$ is smooth and $\det J_F (p) \neq 0$, then for some open neighborhoods of $p$ and $F(p)$ they are related by a diffeomorphic restriction on $F$.

If $F$ is bijective and $\det J_F (p) \neq 0$ for all $p \in U$, then $F$ is a diffeomorphism.


