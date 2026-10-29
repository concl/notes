





## Profiling

PyTorch includes tools for profiling CPU and GPU operations which use context managers. We can profile our code with the following:

```python
import torch
from torch.profiler import profile, ProfilerActivity, record_function

with profile(activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA]) as prof:
	for _ in range(10):
		a = torch.square(torch.randn((50, 50)))
	torch.cuda.synchronize()
	
prof.export_chrome_trace("trace.json")
```

We can open the generated trace in https://ui.perfetto.dev to get something like this (not the same trace, but similar):

![[perfetto_trace.png]]
