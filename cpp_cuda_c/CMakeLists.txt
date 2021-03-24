cmake_minimum_required(VERSION 3.15 FATAL_ERROR)
#cmake_policy(SET CMP0094 NEW)

project(SplinePSF LANGUAGES CXX C)

include(CheckLanguage)
check_language(CUDA)

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)
find_package(CUDA)

if(CMAKE_CUDA_COMPILER AND NOT CUDA_DISABLED)  # the latter is a user definable variable
   enable_language(CUDA)
   add_compile_definitions(CUDA_ENABLED)

   set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} --gpu-architecture=sm_37")

else()
   message(WARNING "No CUDA compiler found or disabled by user defined command line variable '-DCUDA_DISABLED=True'.
   You may need to specify its path according to the CMake instructions applicable to this version.")

endif()


add_library(spline_psf_cpu_impl STATIC src/spline_psf.c)
target_include_directories(spline_psf_cpu_impl PUBLIC include)
target_compile_features(spline_psf_cpu_impl PUBLIC c_std_99)
set_property(TARGET spline_psf_cpu_impl PROPERTY POSITION_INDEPENDENT_CODE ON)

if(CMAKE_CUDA_COMPILER AND NOT CUDA_DISABLED)
   add_library(spline_psf_cu_impl STATIC src/spline_psf_gpu.cu)
   target_include_directories(spline_psf_cu_impl PUBLIC include)
   target_compile_features(spline_psf_cu_impl PUBLIC cxx_std_11)
   set_target_properties(spline_psf_cu_impl PROPERTIES CUDA_SEPARABLE_COMPILATION ON POSITION_INDEPENDENT_CODE ON)

   link_directories(/usr/local/cuda/lib64)
   include_directories("${CUDA_INCLUDE_DIRS}")

   pybind11_add_module(spline src/pybind_spline.cpp)
   target_link_libraries(spline PRIVATE spline_psf_cu_impl spline_psf_cpu_impl)

else()  # NO CUDA

   pybind11_add_module(spline src/pybind_spline.cpp)
   target_link_libraries(spline PRIVATE spline_psf_cpu_impl)

endif()
