# SplinePSF
This is a factored out implementation repository of the spline function implemented in C++/C and CUDA.
Currently it may only be used in conjunction with the DeepSMLM package. However we are planning on small standalone
wrapper for Python / MATLAB.

## Installation

```
conda install -c haydnspass spline
```

### Known Limitations

* C++/CUDA implementation is currently not meant for standalone use
* CUDA does not support ROIs bigger than 32 x 32 = 1024 pixels (this is due to the maximum number of threads per block). Please refer to the CPU version in this case
