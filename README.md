# SplinePSF
This is a factored out implementation repository of the spline function implemented in C++/C and CUDA.
Currently it may only be used in conjunction with the DeepSMLM package. However we are planning on small standalone
wrapper for Python / MATLAB; this is also the reason why we opted for a separate repository.

## Installation

```
conda install -c haydnspass -c conda-forge spline
```

### Known Limitations

* C++/CUDA implementation is currently not ready for standalone use
* Updated: CUDA supports arbitrary ROI size now. ~~CUDA does not support ROIs bigger than 32 x 32 = 1024 pixels (this is due to the maximum number of threads per block). Please refer to the CPU version in this case~~

### Build and Install Python package for Local Use
```bash
python setup.py install
```

### Buildwheels
```bash
python setup.py bdist_wheel
```

### Build and Deploy with conda
```bash
# recommended: create a new conda build environment
conda create --name build_clean conda-build
conda activate build_clean

# navigate to [repo]/conda
cd dist_tools/conda
conda-build -c conda-forge spline
```