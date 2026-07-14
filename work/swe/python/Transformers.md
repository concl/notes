The transformers library is the most standard way to access open weight models for different tasks. It also provides many utilities for data and training. LLM inference is supported, but vLLM provides a better backend.

## Embedding Models

Mostly uses `sentence-transformers`.

Loading a model (notice that it doesn't use the usual `.from_pretrained()` method):
```
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-Embedding-4B")
```

The `Qwen/Qwen3-Embedding` series has prompts that can distinguish between "query" texts and "document" texts, which are stored as a dictionary under `model.prompts`.

To embed a batch of prompts, we can run the following (adding the respective prompts for "queries"):
```python
queries = [
    "What is the capital of China?",
    "Explain gravity",
]
documents = [
    "The capital of China is Beijing.",
    "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun.",
]

query_embeddings = model.encode(queries, prompt_name="query")
document_embeddings = model.encode(documents)
```

To convert to PyTorch tensors for the output, use the `convert_to_tensor` kwarg:
```python
query_embeddings = model.encode(queries, prompt_name="query", convert_to_tensor=True)
document_embeddings = model.encode(documents, convert_to_tensor=True)
```

