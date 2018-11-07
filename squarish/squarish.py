# -*- coding: utf-8 -*-

"""Main module."""

import math
import functools

def squarest_total(m,n,return_greatest=False):
    """Returns the :term:`squarest` integer
    in the range `(m, m + n)` (inclusive).
    
    In the case of several perfect squares,
    the lowest is returned by default.

    Parameters
    ----------

    m : int
        The low end of the range.

    n : int
        The maximum value that can be added to `m`,
        to produce a squarish number.

    return_greatest : bool, optional
        Whether to return the lowest (False, default) or highest (True) 
        in the case of multiple perfect squares within range.

    Examples
    --------

    >>> squarest_total(10,7)
    16

    >>> squarest_total(3,8)
    4

    >>> squarest_total(3,8,return_greatest=True)
    9

    >>> squarest_total(9,27)
    9

    >>> squarest_total(9,27,return_greatest=True)
    36

    >>> squarest_total(37, 10)
    42

    """

    return squarest_of(range(m,m+n+1), reverse_on_key=return_greatest)
        

def squarest_of(c, sort_key=None, reverse_on_key=False):
    """Returns the :term:`squarest` member of `c`, a collection of numbers.

    If there are multiple perfect squares, 
    `sort_key` is used to pick a single one.

    Parameters
    ----------

    c : iterable of int
        A collection of integers.

    sort_key : callable, optional
        Callable used to sort the results 
        in the case of multiple perfect squares.

        By default, the function returns the lowest perfect square.

    reverse_on_key : bool, optional
        Whether to reverse the sort order
        in the case of multiple squares.
    
        When ``False`` is used with the default ``sort_key``,
        the highest perfect square will be returned.

    Examples
    --------

    >>> squarest_of([1,2,3,4,5,6,7,8,9,10,11,12])
    1

    >>> squarest_of([1,2,3,4,5,6,7,8,9,10,11,12],reverse_on_key=True)
    9

    >>> squarest_of([8,10,15,17,24,26,35,37,48,50,63,65])
    63

    >>> squarest_of([x for x in range(2,8000) if is_prime(x)])
    2
    """

    try:
        # Get a perfect square.
        return sorted([x for x in c if is_square(x)], key=sort_key, reverse=reverse_on_key)[0]
    except IndexError:
        # There weren't any perfect squares. Get the squarest.
        return max(c, key=lambda x:squareness(x))
            
        
@functools.lru_cache()
def squarish_factors(x):
    """Returns the closest pair of factors of x.

    Parameters
    ----------

    x : int

    Examples
    --------

    >>> squarish_factors(20)
    (5, 4)

    >>> squarish_factors(36)
    (6, 6)

    >>> squarish_factors(53)
    (53, 1)

    >>> squarish_factors(0)
    (0, 0)

    """
    if is_square(x):
        sr = int(math.sqrt(x))
        return sr, sr
    
    mid = math.floor(math.sqrt(x))

    for d in range(mid,0,-1):
        if x%d == 0:
            return int(x/d),d

    # if the above loop completes, there's a problem
    raise ValueError("X must be a positive integer.")



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

    Examples
    --------

    >>> squareness(1)
    1.0

    >>> squareness(4)
    1.0

    >>> squareness(5) < squareness(12)
    True
    

    """

    
    if x == 0:
        return 1
    sr = math.sqrt(x)
    m,n = squarish_factors(x)
    
    return (sr/m + n/sr)/2

    
    



def r_size(x):
    """Returns the difference between the largest and smallest value in a collection.

    Parameters
    ----------

    x : collection of numbers
    
    Examples
    --------

    >>> r_size([2,4,6,8])
    6

    >>> r_size({3,6,9,11})
    8

    """
    return max(x) - min(x)


def is_square(x):
    """Returns True if x is a perfect square. Otherwise False.

    Examples
    --------
    
    >>> is_square(1)
    True

    >>> is_square(-1)
    False

    >>> is_square(4)
    True
    """

    try:
        return int(math.sqrt(x)) == math.sqrt(x)
    except ValueError:
        return False


def is_prime(x):
    """Returns True if x is prime. Otherwise False.

    Examples
    --------

    >>> is_prime(1)
    True

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(5)
    True

    >>> is_prime(6)
    False

    >>> is_prime(7)
    True

    """

    return min(squarish_factors(x)) == 1

