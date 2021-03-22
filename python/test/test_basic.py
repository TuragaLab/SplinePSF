
def test_basic():
    import spline

    print(f"Spline CUDA compiled: {spline.cuda_compiled}")
    print(f"Spline CUDA is available: {spline.cuda_is_available()}")
