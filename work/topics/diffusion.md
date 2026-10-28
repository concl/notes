
Diffusion (and flow matching) in its essence is a technique that transforms sampling points from one distribution (a prior distribution) to points from another distribution (a target distribution).

With this formulation, we can generate examples from our target distribution by sampling from our prior distribution, and applying the transformation that makes sampling from the prior equivalent to sampling from our target.

Thus, given $x \sim P_{\text {prior}}$, we want to get $y \sim P_{\text{target}}$.

