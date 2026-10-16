
## Definitions

**Frenet-Serret Frame**

The tangent, normal, and binormal vectors to a curve:
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
\frac{dN}{ds} = -\kappa T +\tau B
$$
$$
\frac{dB}{ds} = -\tau N
$$


($\kappa$ = curvature of the curve, $\tau$ is torsion)


**Osculating Plane**

The osculating plane is the plane where a curve is "locally embedded" in 3D space: the tangent and normal vectors span this plane. The binormal vector is orthogonal to this plane.

**Regular**

A curve $r(t$) that is **regular** is a curve that has $r'(t) \ne \mathbf 0$ for all $t$ in its domain. This property can depend on the specific parametrization of the curve, and isn't necessarily an inherent property of the curve.

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



## Notes

**Torsion Properties**
- If $\tau = 0$ uniformly over a curve, then the curve is planar

**Arc Length Parametrization**
- For a curve $\alpha(s)$ parametrized by arc length, we have that $T(s) = \alpha'(s)$. Thus, if we know $T(s)$ we can integrate it to get $\alpha(s)$.

**Tools**
- (In the x-y plane) Let $\theta(s)$ be the angle that the tangent of a curve makes with the x-axis. Then we have: $T(s) = \left(\cos (\theta(s)), \sin (\theta(s))\right)$. Thus, $T'(s) = \theta'(s) \left(-\sin (\theta(s)), \cos (\theta(s))\right)$. And by the Frenet-Serret formula we have $\theta'(s) = \kappa(s)$. 
	- This is useful, because if we know $\kappa(s)$ then we can integrate it to get $\theta(s)$, which gives us an expression for $T(s)$.
-  

