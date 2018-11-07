import math
import functools
import copy
import random

def fittest_total(m,n,r,return_greatest=False):
    """Returns the integer in the range `(m, m + n)` (inclusive),
    which has a pair of factors whose ratio is nearest r.`
    
    In the case of several equally fit possibilities,
    the lowest is returned by default.

    Parameters
    ----------

    m : int
        The low end of the range.

    n : int
        The maximum value that can be added to `m`,
        to produce a fit number.

    r : number or tuple or fraction
        A ratio to fit.

    return_greatest : bool, optional
        Whether to return the lowest (False, default) or highest (True) 
        in the case of multiple equally-fit numbers within range.

    Examples
    --------

    >>> fittest_total(8,4,2)
    8

    >>> fittest_total(8,4,(3,4))
    12

    """

    return fittest_of(range(m,m+n+1), r, reverse_on_key=return_greatest)
        

def fittest_of(c, r, sort_key=None, reverse_on_key=False):
    """Returns the :term:`fittest` member of `c`, a collection of numbers.

    If there are multiple equally fit numbers,
    `sort_key` is used to pick a single one.

    Parameters
    ----------

    c : iterable of int
        A collection of integers.

    r : number or tuple or fraction
        A ratio to fit.

    sort_key : callable, optional
        Callable used to sort the results 
        in the case of multiple equally-fit numbers.

        By default, the function returns the lowest candidate.

    reverse_on_key : bool, optional
        Whether to reverse the sort order
        in the case of multiple candidates.
    
        When ``False`` is used with the default ``sort_key``,
        the highest fit number will be returned.

    Examples
    --------

    >>> fittest_of([1,2,3,4,5,6,7,8,9,10,11,12], 2)
    2

    >>> fittest_of([1,2,3,4,5,6,7,8,9,10,11,12], 2, reverse_on_key=True])
    8

    >>> fittest_of([8,10,15,17,24,26,35,37,48,50,63,65], (3,4))
    48

    """

    raise NotImplementedError


@functools.lru_cache()
def factors_of(x):
    """Returns a set of tuples of factors of x.

    Examples
    --------

    >>> factors_of(12)
    {(1, 12), (2, 6), (3, 4)}

    >>> factors_of(20)
    {(1, 20), (2, 10), (4,5)}
    """

    factors = set()
    sqrt_x = math.sqrt(x)
    if sqrt_x == int(sqrt_x):
        factors.add((sqrt_x, sqrt_x))

    for d in range(math.floor(sqrt_x)): # d for divisor
        if x % d == 0:
            factors.add((d,int(x/d)))

    return factors
    



    
@functools.lru_cache()
def fittest_factors(x, r):
    """Returns the pair of factors of x,
       whose ratio is closest to r.

    Parameters
    ----------

    x : int
    r : number or fraction or tuple

    Examples
    --------

    >>> fittest_factors(20, (6,4))
    (5, 4)

    >>> fittest_factors(36, 1)
    (6, 6)

    >>> squarish_factors(53, 0.9)
    (53, 1)
    """

    raise NotImplementedError

def is_squarish(x, threshold=0.75):
    """Determines whether x is sufficiently squarish.

    Parameters
    ----------

    x : int

    threshold : float, optional
        The lower bound of acceptable squareness.

    Examples
    --------

    >>> is_squarish(67)
    False

    >>> is_squarish(12)
    True
    """

    return squareness(x) > threshold


def squareness(x):
    """Returns a number between ``(0,1)`` 
    representing the squareness of ``x``.

    All perfect squares have a squareness of ``1``.
    

    """

    
    if x == 0:
        return 1
    sr = math.sqrt(x)
    m,n = squarish_factors(x)
    
    return (sr/m + n/sr)/2

    
    


###

def dict_list_append(d, index_of_list, item):
    """Adds an item to a list in a dictionary,
    and creates the list if needed.

    Returns nothing.
    """
    try:
        d[index_of_list].append(item)
    except IndexError:
        d[index_of_list] = [item]


def r_size(x):
    """Returns the difference between the largest and smallest value in a collection."""
    return max(x) - min(x)

def is_square(x):
    """Returns True if x is a perfect square. Otherwise False."""
    return int(math.sqrt(x)) == math.sqrt(x)


def is_prime(x):
    """Returns True if x is prime. Otherwise False."""

    return min(squarish_factors(x)) == 1

