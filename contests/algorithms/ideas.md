
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

Sometimes, when performing operations on an object, a certain property cannot change. This is useful for proving that certain things are impossible and thus do not need to be considered.

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

