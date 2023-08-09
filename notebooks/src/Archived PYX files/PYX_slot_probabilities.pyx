import itertools
from fractions import Fraction
cimport cython

Slot_probabilities = {'red': Fraction(18, 38), 'black': Fraction(18, 38), 'green': Fraction(2, 38)}

@cython.cdivision(True)
def calculate_lengths_cython(int range_start, int range_end):
    cdef list lengths = []
    cdef list elements = []
    cdef int i
    cdef list permutations, combinations, combinations_with_replacement, permutations_with_replacement
    cdef int permutations_len, combinations_len, combinations_with_replacement_len, permutations_with_replacement_len

    for i in range(range_start, range_end + 1):
        permutations = list(itertools.permutations(list(Slot_probabilities.items()), i))
        combinations = list(itertools.combinations(list(Slot_probabilities.items()), i))
        combinations_with_replacement = list(itertools.combinations_with_replacement(list(Slot_probabilities.items()), i))
        permutations_with_replacement = list(itertools.product(list(Slot_probabilities.items()), repeat=i))

        permutations_len = len(permutations)
        combinations_len = len(combinations)
        combinations_with_replacement_len = len(combinations_with_replacement)
        permutations_with_replacement_len = len(permutations_with_replacement)

        lengths.append((permutations_len, combinations_len, combinations_with_replacement_len, permutations_with_replacement_len))
        elements.append((permutations, combinations, combinations_with_replacement, permutations_with_replacement))

    return list(range(range_start, range_end + 1)), lengths, elements
