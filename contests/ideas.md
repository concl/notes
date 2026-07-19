
## Problem Types

### [[construction]]: 
Building a thing that satisfies some property




## Problem Solving Techniques

### [[transformation]]: 
When a problem has a certain type of object of interest (i.e. an array, graph, string, parentheses string), we can often apply a transformation on this object (i.e. build a prefix sum) for which the same dynamics of the problem play nicer.

- If the problem involves applying some operation to the object, we can think about what happens to the transformed object after this operation.
- If the problem involves considering some property of the object, we can think about how we check for this property in the transformed object.

### considering small cases


### 


### considering a general case

Sometimes a problem can be thought of as a special case of a general problem. If this general problem is known to be (or seems to be) hard, what makes the special case easier?
- Maybe there's a restriction on the possibilities on the solution (something might be greedy). For instance, for an alternating sum of a subsequence of an array, if the array is strictly increasing then the sum can't be 0. If the array is increasing non strictly then the subsequence must have an even number of each unique element.

### casework

Sometimes the problem can be broken down into cases. Generally, considering one case is strictly easier than considering the problem as a whole.