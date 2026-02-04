# PyTorch Tensor Manipulation Exercises

Welcome to the comprehensive PyTorch tensor manipulation exercise series! This collection is designed to take you from beginner to expert level in PyTorch tensor operations.

## 📚 Exercise Structure

### 🟢 Basic Level (`01_basic_tensor_exercises.md`)
**Target Audience**: Complete beginners to PyTorch
**Prerequisites**: Basic Python knowledge
**Topics Covered**:
- Tensor creation (zeros, ones, arange, eye)
- Data type conversions
- Basic indexing and slicing
- Reshaping and viewing
- Element-wise operations
- Concatenation and stacking
- Finding max/min values
- Boolean indexing
- Squeezing and unsqueezing
- Basic broadcasting

**Estimated Time**: 2-3 hours

### 🟡 Medium Level (`02_medium_tensor_exercises.md`)
**Target Audience**: Students with basic PyTorch knowledge
**Prerequisites**: Completed basic exercises, understanding of tensor shapes
**Topics Covered**:
- Advanced indexing and fancy indexing
- Multi-dimensional broadcasting
- Gradient computation basics (`requires_grad`)
- Tensor permutation and transposition
- Statistical operations and reductions
- Tensor splitting and chunking
- Conditional operations (`torch.where`)
- Matrix operations and linear algebra
- Memory layout and performance
- Custom tensor functions

**Estimated Time**: 4-5 hours

### 🔴 Advanced Level (`03_advanced_tensor_exercises.md`)
**Target Audience**: Advanced users and researchers
**Prerequisites**: Strong linear algebra, deep learning concepts, completed medium exercises
**Topics Covered**:
- Custom autograd functions
- Einstein summation (`torch.einsum`)
- Memory-efficient operations
- Complex gradient computations
- Tensor decomposition and advanced linear algebra
- Sparse tensors and advanced indexing
- Parallel and distributed operations
- Custom loss functions and metrics
- Numerical stability
- Research-level tensor transformations

**Estimated Time**: 6-8 hours

## 🚀 Getting Started

### Installation Requirements
```bash
pip install torch torchvision numpy matplotlib
```

### Recommended Learning Path
1. **Start with Basic**: Even if you have some PyTorch experience, review the basic exercises to ensure solid fundamentals
2. **Progress Sequentially**: Each level builds upon the previous one
3. **Practice Regularly**: Try to complete a few exercises each day rather than all at once
4. **Experiment**: Modify the exercises with different tensor sizes and parameters
5. **Read Documentation**: Use the official PyTorch documentation when stuck

### How to Use These Exercises
1. **Read the Task**: Understand what you need to accomplish
2. **Try First**: Attempt the exercise before looking at solutions
3. **Check Solutions**: Compare your approach with the provided solutions
4. **Experiment**: Modify the code to deepen understanding
5. **Time Yourself**: Track how long exercises take to gauge progress

## 📖 Learning Objectives

By completing all three levels, you will:

### Basic Level Objectives
- [ ] Create tensors using various methods
- [ ] Perform basic tensor manipulations
- [ ] Understand tensor shapes and dimensions
- [ ] Apply element-wise operations
- [ ] Use basic indexing and slicing
- [ ] Understand broadcasting fundamentals

### Medium Level Objectives
- [ ] Master advanced indexing techniques
- [ ] Understand gradient computation
- [ ] Perform complex tensor transformations
- [ ] Apply statistical operations efficiently
- [ ] Handle memory and performance considerations
- [ ] Create custom tensor functions

### Advanced Level Objectives
- [ ] Implement custom autograd functions
- [ ] Master Einstein summation notation
- [ ] Optimize for memory and performance
- [ ] Handle numerical stability issues
- [ ] Work with sparse tensors
- [ ] Implement research-level operations

## 🛠️ Tips for Success

### General Tips
1. **Use Jupyter Notebooks**: Interactive development helps with learning
2. **Print Shapes**: Always check tensor shapes with `.shape` or `.size()`
3. **Start Small**: Begin with small tensors to understand operations
4. **Read Error Messages**: PyTorch error messages are usually helpful
5. **Use Documentation**: The PyTorch docs are excellent

### Debugging Tips
1. **Check Dimensions**: Most errors are dimension mismatches
2. **Verify Data Types**: Ensure compatible data types for operations
3. **Use `.clone()`**: When you need independent copies of tensors
4. **Check Device**: Ensure tensors are on the same device (CPU/GPU)

### Performance Tips
1. **Batch Operations**: Vectorize operations when possible
2. **Avoid Loops**: Use tensor operations instead of Python loops
3. **In-place Operations**: Use `_` suffix for memory efficiency (when safe)
4. **Profile Code**: Use timing to identify bottlenecks

## 🎯 Assessment and Progress Tracking

### Self-Assessment Questions
After each level, ask yourself:
- Can I complete the exercises without looking at solutions?
- Do I understand why each operation works?
- Can I modify the exercises with different parameters?
- Can I explain the concepts to someone else?

### Progress Milestones
- [ ] **Basic Complete**: Can create and manipulate tensors confidently
- [ ] **Medium Complete**: Understand gradients and advanced operations
- [ ] **Advanced Complete**: Can implement custom operations and optimize performance

## 🔗 Additional Resources

### Official Documentation
- [PyTorch Tensors](https://pytorch.org/docs/stable/tensors.html)
- [Autograd](https://pytorch.org/docs/stable/autograd.html)
- [torch.nn.functional](https://pytorch.org/docs/stable/nn.functional.html)

### Recommended Reading
- PyTorch official tutorials
- "Deep Learning with PyTorch" book
- PyTorch forums and community discussions

### Practice Projects
After completing these exercises, consider:
1. Implementing a simple neural network from scratch
2. Creating custom loss functions
3. Building data preprocessing pipelines
4. Optimizing existing PyTorch code

## 🤝 Contributing

Found an error or have suggestions for improvement? Feel free to:
- Report issues with specific exercises
- Suggest additional exercises
- Provide alternative solutions
- Share your learning experience

## 📝 Notes

- All exercises are designed to be educational and practical
- Solutions are provided but try to solve them independently first
- Exercises progress from fundamental concepts to research-level operations
- Each exercise builds upon previous knowledge
- Focus on understanding concepts, not just completing tasks

Happy learning! 🎉
