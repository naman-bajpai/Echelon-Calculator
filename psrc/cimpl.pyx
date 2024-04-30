# cimpl.pyx

cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cdef double calculate_mean(double[:] data):
    cdef double sum = 0.0
    cdef int count = 0
    
    for value in data:
        sum += value
        count += 1
        
    if count > 0:
        return sum / count
    else:
        return 0.0

def process_data(filename):
    cdef np.ndarray[np.double_t, ndim=1] data = np.loadtxt(filename)
    return calculate_mean(data)
