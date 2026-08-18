Dynamic programming is a technique for solving problems where we define some notion of state, where each state represents a subproblem (the full problem instance will be encoded in one such state).

Each state is typically dependent on some number of other states, and this dependency graph is a DAG. Thus, we can solve the full problem by traversing this graph topologically, starting from the nodes that have no dependencies on other states (base cases which can be solved directly).

## Notes

For problems where the state is a subarray of a larger array, if the relationship is between larger arrays to subarrays inside the larger array, it's usually easier to implement a solution that starts with smaller arrays and builds larger arrays from the smaller arrays.