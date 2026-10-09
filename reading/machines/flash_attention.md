
Video Ref: https://www.youtube.com/watch?v=gBMO1JZav44

Standard attention implemented naively is highly inefficient and slow. 

Computing:
$$
\text{Attention}(Q, K, V) = \text{softmax}(\frac{QK^\top}{\sqrt d_{\text{model}}})V
$$

Requires the following steps:

```mermaid
flowchart TD
    A["Load Q, K from HBM"]
    B["Compute S = QKᵀ / √d_model"]
    C["Store S into HBM"]
    D["Load S from HBM"]
    E["Compute A = softmax(S)"]
    F["Store A into HBM"]
    G["Load A, V from HBM"]
    H["Compute O = AV"]
    I["Store O into HBM"]

    A --> B --> C --> D --> E --> F --> G --> H --> I
```
