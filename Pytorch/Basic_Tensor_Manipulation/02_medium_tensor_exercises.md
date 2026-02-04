# Medium PyTorch Tensor Manipulation Exercises

These medium-level exercises will challenge you with more complex tensor operations commonly used in deep learning applications.

## Prerequisites
- Completed basic tensor exercises
- Understanding of tensor shapes and basic operations
- Familiarity with NumPy (helpful but not required)

## Import Statement
```python
import torch
import numpy as np
import torch.nn.functional as F
```

---

## Exercise 1: Advanced Indexing and Fancy Indexing

**Task**: 
1. Create a 5x5 tensor with values from 1 to 25
2. Use fancy indexing to extract elements at positions [(0,1), (2,3), (4,0)]
3. Extract all elements from rows [1, 3] and columns [0, 2, 4]
4. Use boolean indexing to find all elements divisible by 3
5. Replace all even numbers with -1

**Advanced Indexing Example**:
```python
tensor = torch.arange(1, 26).reshape(5, 5)
# Your advanced indexing here
```

---

## Exercise 2: Tensor Broadcasting with Multiple Dimensions

**Task**: 
1. Create tensor A of shape (2, 1, 4)
2. Create tensor B of shape (3, 1)
3. Create tensor C of shape (1, 5, 1)
4. Perform A + B, A * C, and A + B + C
5. Explain the resulting shapes and how broadcasting worked

**Challenge**: Predict the output shapes before running the code!

---

## Exercise 3: Gradient Computation Basics

**Task**: 
1. Create a tensor x with `requires_grad=True` and values [1.0, 2.0, 3.0]
2. Compute y = x² + 2x + 1
3. Compute the gradient of y with respect to x
4. Create a more complex function: z = (x³ - 2x²).sum()
5. Compute gradients and verify manually for one value

**Key Concepts**: `requires_grad`, `.backward()`, `.grad`

---

## Exercise 4: Tensor Permutation and Transposition

**Task**: 
1. Create a 4D tensor of shape (2, 3, 4, 5)
2. Transpose the last two dimensions
3. Permute dimensions to order (3, 1, 0, 2)
4. Flatten the tensor while preserving the first dimension
5. Reshape back to original shape and verify equality

**Functions**: `.transpose()`, `.permute()`, `.flatten()`, `.contiguous()`

---

## Exercise 5: Statistical Operations and Reductions

**Task**: Create a 3D tensor of shape (4, 5, 6) with random values, then compute:
1. Mean along each dimension separately
2. Standard deviation along the last dimension
3. Cumulative sum along dimension 1
4. Variance across all elements
5. Median along dimension 0 (use `torch.median`)

**Bonus**: Compare results with NumPy equivalents

---

## Exercise 6: Tensor Splitting and Chunking

**Task**: 
1. Create a tensor of shape (12, 8)
2. Split it into 3 equal parts along dimension 0
3. Split it into chunks of size 3 along dimension 1
4. Use `torch.split()` with different sizes: [2, 4, 6]
5. Reconstruct the original tensor from the splits

**Functions**: `torch.split()`, `torch.chunk()`, `torch.cat()`

---

## Exercise 7: Conditional Operations and Where

**Task**: 
1. Create two random tensors A and B of shape (4, 4)
2. Use `torch.where()` to create a tensor that takes values from A where A > 0.5, else from B
3. Create a tensor that replaces negative values with 0 and positive values with 1
4. Implement a custom "clamp" function using `torch.where()`
5. Create a tensor with alternating values based on index position

---

## Exercise 8: Matrix Operations and Linear Algebra

**Task**: 
1. Create two matrices A (3x4) and B (4x5)
2. Perform batch matrix multiplication with 3D tensors
3. Compute the determinant of a 3x3 matrix
4. Find eigenvalues and eigenvectors of a symmetric matrix
5. Solve a system of linear equations Ax = b

**Functions**: `torch.matmul()`, `torch.det()`, `torch.eig()`, `torch.solve()`

---

## Exercise 9: Tensor Memory Layout and Performance

**Task**: 
1. Create a large tensor (1000, 1000) and time different operations
2. Compare performance of `.view()` vs `.reshape()`
3. Understand when `.contiguous()` is needed
4. Create tensors with different memory layouts and measure access patterns
5. Implement a function that checks if a tensor is contiguous

**Performance Focus**: Understanding memory efficiency in PyTorch

---

## Exercise 10: Custom Tensor Operations and Functions

**Task**: 
1. Implement a function that normalizes a tensor to have mean=0 and std=1
2. Create a function that applies softmax along a specified dimension
3. Implement a custom distance function (Euclidean distance between rows)
4. Create a function that finds the k-nearest neighbors in a tensor
5. Implement a sliding window operation on a 1D tensor

**Example Template**:
```python
def normalize_tensor(tensor, dim=None):
    """Normalize tensor to have mean=0 and std=1"""
    # Your implementation here
    pass

def custom_softmax(tensor, dim=-1):
    """Implement softmax function"""
    # Your implementation here
    pass
```

---

## Solutions

<details>
<summary>Click to see solutions (try the exercises first!)</summary>

### Exercise 1 Solution:
```python
# Create 5x5 tensor
tensor = torch.arange(1, 26).reshape(5, 5)
print("Original tensor:\n", tensor)

# Fancy indexing for specific positions
rows = torch.tensor([0, 2, 4])
cols = torch.tensor([1, 3, 0])
elements = tensor[rows, cols]
print("Elements at specific positions:", elements)

# Extract rows and columns
subset = tensor[[1, 3]][:, [0, 2, 4]]
print("Subset:\n", subset)

# Boolean indexing for divisible by 3
divisible_by_3 = tensor[tensor % 3 == 0]
print("Divisible by 3:", divisible_by_3)

# Replace even numbers with -1
tensor_modified = tensor.clone()
tensor_modified[tensor_modified % 2 == 0] = -1
print("Even numbers replaced:\n", tensor_modified)
```

### Exercise 3 Solution:
```python
# Create tensor with gradient tracking
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Compute y = x² + 2x + 1
y = x**2 + 2*x + 1
print("y =", y)

# Compute gradients
y.sum().backward()
print("Gradient of y w.r.t. x:", x.grad)

# Reset gradients for next computation
x.grad.zero_()

# More complex function
z = (x**3 - 2*x**2).sum()
z.backward()
print("Gradient of z w.r.t. x:", x.grad)
```

</details>

---

## Key Concepts Covered
- Advanced indexing and slicing
- Broadcasting with multiple dimensions
- Gradient computation basics
- Tensor permutations and memory layout
- Statistical operations and reductions
- Conditional operations
- Linear algebra operations
- Performance considerations
- Custom tensor functions

## Tips for Success
1. Always verify tensor shapes after operations
2. Use `.clone()` when you need to modify tensors without affecting originals
3. Pay attention to gradient flow in autograd operations
4. Understand when operations create new tensors vs. modify existing ones
5. Practice with different tensor sizes to understand scalability

## Next Steps
Ready for advanced exercises? Move on to the advanced-level exercises for expert-level tensor manipulation!
