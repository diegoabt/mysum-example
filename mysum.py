def my_sum(numbers):
    """Returns the sum of all elements in the iterable.
    Returns None if the argument is not a list, tuple, or set,
    or if any element is not an int or float.
    """
    # Check input type, return None if type is not correct
    if not isinstance(numbers, (list, tuple, set)):
        return None
    if not all(isinstance(n, (int, float)) for n in numbers):
        return None
    total = 0
    # This is the core of the function
    for n in numbers:
        total += n
    return total
