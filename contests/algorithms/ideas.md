
## Problem Types

### [[construction]]: 
Building a thing that satisfies some property




## Problem Solving Techniques

### [[transformation]]: 
When a problem has a certain type of object of interest (i.e. an array, graph, string, parentheses string), we can often apply a transformation on this object (i.e. build a prefix sum) for which the same dynamics of the problem play nicer.

- If the problem involves applying some operation to the object, we can think about what happens to the transformed object after this operation.
- If the problem involves considering some property of the object, we can think about how we check for this property in the transformed object.

### considering small cases

Small cases of a problem can reveal a large amount of structure of the general problem. In some cases, a problem can be decomposed entirely into finitely many small cases.

### considering a general case

Sometimes a problem can be thought of as a special case of a general problem. If this general problem is known to be (or seems to be) hard, what makes the special case easier?
- Maybe there's a restriction on the possibilities on the solution (something might be greedy). For instance, for an alternating sum of a subsequence of an array, if the array is strictly increasing then the sum can't be 0 (an invariant). If the array is increasing non strictly then the subsequence must have an even number of each unique element.

### casework

Sometimes the problem can be broken down into cases. Generally, considering one case is strictly easier than considering the problem as a whole.

## invariants

Sometimes, when performing operations on an object, a certain property cannot change. This is useful for proving that certain things are impossible and thus do not need to be considered. This is also a strategy to find arguments for greedy algorithms.

Example:
Problem: https://open.kattis.com/contests/wiu64b/problems/incrementalinduction
In this problem, the key observation is that once the first contestant is chosen, every time another contestant is added, the current $k$ is updated only depending on the number of games that this contestant has won. 

We can think of this in terms of invariants by first considering the number of games that have been lost by each contestant in our stage set, $S$ (which starts empty, and accumulates players according to the order in which contestants are added). Denote this as $L(S) = \sum L(S_i)$ where $L(S_i)$ is the number of games that the $i$th contestant lost. 

The number of "bad games" is thus this quantity minus the number of losses that are between contestants in $S$. Since each game always end in a win or loss, the number of losses between contestants in $S$ is always $\binom{|S|}{2}$.

Thus we have a formula for the number of bad games at any point in time (where $t$ represents the number of contestants that we have added so far, $|S| = t$):
$$
\text{badgames}(t) = \sum L(S_i) - \binom{t}{2}
$$
This gives us an easy recurrence relation that allows us to compute the number of bad games at every point in time quickly. Furthermore, the optimal order is one where contestants that have less losses than other contestants go first.
## symmetry

Symmetry can be often used to optimize resource complexity.

## working backwards

In problems that require finding a "path" to a solution, it can be much easier to start from the solution and reconstruct the "path" backwards.

# Specific problem topics

## XOR

Many problems involve taking bitwise xor's of integers that are a part of some object. XOR is a commutative and associative operation where every integer is its own inverse; algebraic reasoning a common first approach to problems involving xor.

This is a very common problem topic which usually involves making a number of observations; often problems require simplifying what exactly xor means in context. 

Commonly utilized ideas/tricks/properties of xor:
- For a cumulative xor of a (multi)set of elements, elements that appear an even amount of times will be canceled out. (This property can be used to isolate a single element that satisfies some property).
- Simulate/write down the set of xor operations algebraically to see if there are any cancellations/invariants
- Sometimes considering simple boolean variables only (instead of full bit strings) can reveal a lot about the structure of the problem

