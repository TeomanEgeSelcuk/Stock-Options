# cython_numpy_test.pyx
import numpy as np
cimport numpy as np

# Define a Cython function that calculates the element-wise product of two arrays
def elementwise_product():
    cdef int length = 3  # Predefined length for the arrays
    cdef np.ndarray[np.float64_t, ndim=1] array1 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    cdef np.ndarray[np.float64_t, ndim=1] array2 = np.array([4.0, 5.0, 6.0], dtype=np.float64)
    
    cdef np.ndarray[np.float64_t, ndim=1] result = np.empty(length, dtype=np.float64)

    for i in range(length):
        result[i] = array1[i] * array2[i]

    return result

if __name__ == "__main__":
    elementwise_product()