# cython: language_level=3
    
import numpy as np
cimport numpy as np

# Cython function for permutations with replacement
cpdef np.ndarray[np.object_] cython_permutations(np.ndarray arr, int r):
    cdef int i, j
    cdef int n = arr.shape[0]
    cdef np.ndarray[np.object_] result = np.empty((n ** r, r), dtype=np.object_)
    cdef np.ndarray[np.int32_t] indices = np.arange(n, dtype=np.int32)

    cdef np.ndarray[np.int32_t, ndim=2] combs = np.empty((n ** r, r), dtype=np.int32)
    cdef int div = n

    for j in range(r):
        div //= n
        combs[:, j] = indices // div
        indices = indices % div

    for i in range(n ** r):
        result[i] = arr[combs[i]]

    return result

# Cython function for combinations without replacement
cpdef np.ndarray[np.object_] cython_combinations(np.ndarray arr, int r):
    cdef int i, j
    cdef int n = arr.shape[0]
    cdef np.ndarray[np.object_] result = np.empty((n * (n - 1) // 2, r), dtype=np.object_)
    cdef np.ndarray[np.int32_t] indices = np.arange(n, dtype=np.int32)
    cdef int count = 0

    cdef np.ndarray[np.int32_t, ndim=2] combs = np.empty((n * (n - 1) // 2, r), dtype=np.int32)

    for i in range(n - 1):
        for j in range(i + 1, n):
            combs[count] = np.array([i, j], dtype=np.int32)
            count += 1

    for i in range(count):
        result[i] = arr[combs[i]]

    return result

# Cython function for combinations with replacement
cpdef np.ndarray[np.object_] cython_combinations_with_replacement(np.ndarray arr, int r):
    cdef int i, j
    cdef int n = arr.shape[0]
    cdef np.ndarray[np.object_] result = np.empty((n * (n + r - 1) // r, r), dtype=np.object_)
    cdef np.ndarray[np.int32_t] indices = np.arange(n, dtype=np.int32)
    cdef int count = 0

    cdef np.ndarray[np.int32_t, ndim=2] combs = np.empty((n * (n + r - 1) // r, r), dtype=np.int32)

    for i in range(n ** r):
        for j in range(r):
            combs[count, j] = indices[i // (n ** (r - j - 1)) % n]
        count += 1

    for i in range(count):
        result[i] = arr[combs[i]]

    return result

# Cython function for combinations without replacement
cpdef np.ndarray[np.object_] cython_combinations_without_replacement(np.ndarray arr, int r):
    cdef int i, j, k
    cdef int n = arr.shape[0]
    cdef np.ndarray[np.object_] result = np.empty((n * (n - 1) * (n - 2) // (3 * 2 * 1), r), dtype=np.object_)
    cdef np.ndarray[np.int32_t] indices = np.arange(n, dtype=np.int32)
    cdef int count = 0

    cdef np.ndarray[np.int32_t, ndim=2] combs = np.empty((n * (n - 1) * (n - 2) // (3 * 2 * 1), r), dtype=np.int32)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                combs[count] = np.array([i, j, k], dtype=np.int32)
                count += 1

    for i in range(count):
        result[i] = arr[combs[i]]

    return result
