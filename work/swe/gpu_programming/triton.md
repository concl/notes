[[python]]
Main Docs: https://triton-lang.org/main/index.html


## Introduction

Triton is a language that helps programmers write GPU kernels. It uses a JIT which is a function decorator for python functions.

A Triton kernel looks like:

```python
import triton_language as tl

@triton.jit
def foo(x_ptr):
	pass
```

With CUDA, the kernel is written from the perspective of a single **thread**. A kernel launch is a grid of blocks, and each block has threads which can share data with each other. In Triton, the kernel is written from the perspective of a single **block**, and numpy/torch style operations are performed on a block of data as the input.

## Launching a kernel

A triton kernel is launched like the following:

```python
x = torch.ones(64, 64)
foo[(grid_dim_x, grid_dim_y, grid_dim_z)](x)
```

## Writing a kernel

A kernel is written from the perspective of a block (a program instance), so it needs to know its index within the grid. The index can be obtained as follows:

```python
@triton.jit
def foo(x_ptr):
	block_x = tl.program_id(axis=0)
	block_y = tl.program_id(axis=1)
	block_z = tl.program_id(axis=2)
```

## Main Operations

`tl.load(ptr + arange, mask, other)`:  Loads elements from a tensor ptr (with an arange, which is a tensor from 0 to n) to GPU registers. `other` replaces masked elements.

Example:

```python
@triton.jit
def demo(x_ptr):

    range = tl.arange(0, 8)
    # print works in the interpreter
    print(range)
    x = tl.load(x_ptr + range, range < 5, 2)
    print(x)

demo[(1, 1, 1)](torch.ones(4, 3))
```


`tl.store(ptr + arange, value_to_store, mask)`:  Writes 