
It's often easier to check certain things than it is to relook through the code step by step until a bug is found.
## checklist

Before submitting code to programming contests check the following:

Most Important  (step by step):
1. Make sure sample test cases are completely correct (pay extra attention to formatting)
	- Subpoint: Common mistake is forgetting to take in input, this often fails sample but this should still be checked in the rare case that sample is unavailable or something unlucky.
2. 64 bit integer overflow (any usage of 32 bit integers can be problematic)
	- The pattern `1 << bits` can easily overflow as the literal `1` is 32 bit. Use: `1LL << bits` for 64 bits.
3. **Bitwise order of ops**: Very important. `x & 1 == 0` always evaluates to 0 since `1 == 0` comes first. Use `(x & 1) == 0`. In general use many brackets when working with bitwise ops.
4. Make sure you used modulo operations everywhere if necessary
5. If worried about reading comprehension, check for things like constraints, 
## Common Bugs

One of my most common mistakes is forgetting to take in input. This often leads to a failed sample test (but in rare unlucky instances, it's possible that sample still works, so it's good to always check that all inputs are consumed).
- It's possible that only 1 path skips taking in input, and sample doesn't really test that path.
- To prevent input errors, always take in all input in the beginning, try not to take in input while doing processing steps unless it's trivial.
## Edge Cases

The most common edge case is when the input is "empty". It's common for this edge case to be hidden in the problem statement.

Other Examples:
In an ICPC unit conversion problem, we can build a data structure that allows for conversions between different units in the same group, and if they aren't in the same group, we return this information.

However, the problem statement allowed for conversions between the same unit even if there were no conversion rules for this unit given, for which the correct answer involved returning the quantity unchanged.