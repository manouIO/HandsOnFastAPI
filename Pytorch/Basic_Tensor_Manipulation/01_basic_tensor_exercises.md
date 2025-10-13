# Basic PyTorch Tensor Manipulation Exercises

Welcome to the basic level PyTorch tensor exercises! These exercises will help you get familiar with fundamental tensor operations that form the foundation of deep learning.

## Prerequisites
- Basic Python knowledge
- PyTorch installed (`pip install torch`)

## Import Statement
```python
import torch
import numpy as np
```

---

## Exercise 1: Creating Basic Tensors

**Task**: Create the following tensors and print their shapes:
1. A tensor filled with zeros of shape (3, 4)
2. A tensor filled with ones of shape (2, 3, 4)
3. A tensor with values from 0 to 9 (use `torch.arange`)
4. An identity matrix of size 5x5

**Expected Output Format**:
```python
# Your code here
print("Zeros tensor shape:", zeros_tensor.shape)
print("Ones tensor shape:", ones_tensor.shape)
print("Range tensor:", range_tensor)
print("Identity matrix shape:", identity_matrix.shape)
```

---

## Exercise 2: Tensor Data Types and Conversion

**Task**: 
1. Create a tensor with integers [1, 2, 3, 4, 5]
2. Convert it to float32
3. Convert it to float64
4. Print the data type of each tensor

**Hint**: Use `.dtype` to check data type and `.to()` or `.float()`, `.double()` for conversion.

---

## Exercise 3: Basic Tensor Indexing and Slicing

**Task**: Given a tensor created with `torch.arange(24).reshape(4, 6)`:
1. Extract the first row
2. Extract the last column
3. Extract the element at position (2, 3)
4. Extract a 2x2 submatrix from the center

**Expected Operations**:
```python
tensor = torch.arange(24).reshape(4, 6)
# Your slicing operations here
```

---

## Exercise 4: Tensor Reshaping and Viewing

**Task**: 
1. Create a tensor of shape (2, 3, 4) filled with random values
2. Reshape it to (6, 4)
3. View it as (24,) - a 1D tensor
4. Reshape it back to (2, 3, 4)
5. Verify that the original and final tensors are the same

**Note**: Understand the difference between `.reshape()` and `.view()`

---

## Exercise 5: Basic Mathematical Operations

**Task**: Create two tensors A and B of shape (3, 3) with random values, then perform:
1. Element-wise addition
2. Element-wise multiplication
3. Matrix multiplication
4. Element-wise division
5. Square root of tensor A

**Bonus**: Try both operator syntax (`+`, `*`) and function syntax (`torch.add()`, `torch.mul()`)

---

## Exercise 6: Tensor Concatenation and Stacking

**Task**: 
1. Create three tensors of shape (2, 3) with different values
2. Concatenate them along dimension 0 (rows)
3. Concatenate them along dimension 1 (columns)
4. Stack them to create a 3D tensor

**Functions to use**: `torch.cat()`, `torch.stack()`

---

## Exercise 7: Finding Maximum and Minimum Values

**Task**: Create a random tensor of shape (4, 5), then:
1. Find the maximum value in the entire tensor
2. Find the minimum value in the entire tensor
3. Find the indices of the maximum value
4. Find the maximum value along each row (dim=1)
5. Find the minimum value along each column (dim=0)

---

## Exercise 8: Boolean Indexing and Filtering

**Task**: 
1. Create a random tensor of shape (5, 5) with values between 0 and 1
2. Create a boolean mask for values greater than 0.5
3. Extract all values greater than 0.5
4. Set all values less than 0.3 to zero
5. Count how many values are greater than 0.7

---

## Exercise 9: Tensor Squeezing and Unsqueezing

**Task**: 
1. Create a tensor of shape (1, 5, 1, 3)
2. Remove all dimensions of size 1 using `squeeze()`
3. Add a new dimension at position 0 using `unsqueeze()`
4. Add dimensions at positions 1 and 3 to make it shape (1, 1, 5, 1, 3)

---

## Exercise 10: Basic Broadcasting

**Task**: 
1. Create tensor A of shape (3, 1) with values [[1], [2], [3]]
2. Create tensor B of shape (1, 4) with values [[10, 20, 30, 40]]
3. Add A and B together (observe broadcasting)
4. Multiply A and B together
5. Explain the resulting shapes and values

**Expected Result Shape**: (3, 4)

---

## Solutions

<details>
<summary>Click to see solutions (try the exercises first!)</summary>

### Exercise 1 Solution:
```python
import torch

# 1. Zeros tensor
zeros_tensor = torch.zeros(3, 4)
print("Zeros tensor shape:", zeros_tensor.shape)

# 2. Ones tensor
ones_tensor = torch.ones(2, 3, 4)
print("Ones tensor shape:", ones_tensor.shape)

# 3. Range tensor
range_tensor = torch.arange(10)
print("Range tensor:", range_tensor)

# 4. Identity matrix
identity_matrix = torch.eye(5)
print("Identity matrix shape:", identity_matrix.shape)
```

### Exercise 2 Solution:
```python
# Create integer tensor
int_tensor = torch.tensor([1, 2, 3, 4, 5])
print("Original dtype:", int_tensor.dtype)

# Convert to float32
float32_tensor = int_tensor.float()
print("Float32 dtype:", float32_tensor.dtype)

# Convert to float64
float64_tensor = int_tensor.double()
print("Float64 dtype:", float64_tensor.dtype)
```

### Exercise 3 Solution:
```python
tensor = torch.arange(24).reshape(4, 6)
print("Original tensor:\n", tensor)

# Extract first row
first_row = tensor[0, :]  # or tensor[0]
print("First row:", first_row)

# Extract last column
last_column = tensor[:, -1]
print("Last column:", last_column)

# Extract element at (2, 3)
element = tensor[2, 3]
print("Element at (2,3):", element)

# Extract 2x2 submatrix from center
center_matrix = tensor[1:3, 2:4]
print("Center 2x2 matrix:\n", center_matrix)
```

### Exercise 4 Solution:
```python
# Create original tensor
original = torch.randn(2, 3, 4)
print("Original shape:", original.shape)

# Reshape to (6, 4)
reshaped = original.reshape(6, 4)
print("Reshaped to (6, 4):", reshaped.shape)

# View as 1D
viewed_1d = reshaped.view(24)
print("Viewed as 1D:", viewed_1d.shape)

# Reshape back
back_to_original = viewed_1d.reshape(2, 3, 4)
print("Back to original shape:", back_to_original.shape)

# Verify equality
print("Tensors are equal:", torch.equal(original, back_to_original))
```

### Exercise 5 Solution:
```python
# Create two random tensors
torch.manual_seed(42)
A = torch.randn(3, 3)
B = torch.randn(3, 3)

# Element-wise operations
addition = A + B  # or torch.add(A, B)
multiplication = A * B  # or torch.mul(A, B)
matrix_mult = A @ B  # or torch.matmul(A, B)
division = A / B  # or torch.div(A, B)
sqrt_A = torch.sqrt(torch.abs(A))  # abs to avoid negative sqrt

print("Addition result shape:", addition.shape)
print("Matrix multiplication shape:", matrix_mult.shape)
```

</details>

---

## Tips for Success
1. Always check tensor shapes using `.shape` or `.size()`
2. Use `print()` statements to understand what's happening
3. Experiment with different tensor sizes
4. Read PyTorch documentation when stuck
5. Practice these operations until they become second nature

## Next Steps
Once you've completed these basic exercises, move on to the medium-level exercises to learn more advanced tensor operations!
