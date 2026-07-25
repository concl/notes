
## Max flow

A flow network is a directed graph with a source node and a sink node (s and t) where each edge has a capacity c.

```mermaid
graph LR
    S((S)) -->|10| A((A))
    S -->|8| B((B))
    A -->|5| C((C))
    A -->|5| D((D))
    B -->|4| D
    C -->|6| T((T))
    D -->|9| T
```

The max flow problem asks what is the maximum amount of flow (the amount of outflow from the source) that the network can support. 

```mermaid
graph LR
    S((S)) -->|"10/10"| A((A))
    S -->|"4/8"| B((B))
    A -->|"5/5"| C((C))
    A -->|"5/5"| D((D))
    B -->|"4/4"| D
    C -->|"5/6"| T((T))
    D -->|"9/9"| T
```

More specifically, a flow assigns each edge a value less than its capacity, where (excluding the source and sink) the amount of flow coming into each node is equal to the amount of flow coming out of each node.

## Applications




## Algorithm to compute max flow

The main algorithm used to compute max flow is Dinic's algorithm.