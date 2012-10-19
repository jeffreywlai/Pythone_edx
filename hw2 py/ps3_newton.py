def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.

    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    acc = 0
    for i in range(len(poly)):
        acc += poly[i] * (x)**i
    return float(acc)


def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
 
    >>> print computeDeriv([-13.39, 0.0, 17.5, 3.0, 1.0])
    [0.0, 35.0, 9.0, 4.0]
    >>> print computeDeriv([6, 1, 3, 0])
    [1.0, 6.0, 0.0]
    >>> print computeDeriv([20])
    [0.0]
 
    '''
 
    res = []
    b = 0
    for a in poly:
        if b > 0:
            res = res + [float(a * b)]
        b += 1
    if len(res) == 0:
        return [0.0]
    return res

def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.

    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    i = 0
    def calRoot(poly, x_0, epsilon, i):
        x_n = x_0 - evaluatePoly(poly, x_0) / evaluatePoly(computeDeriv(poly), x_0)
        if (abs(evaluatePoly(poly, x_0)) < epsilon):
            return [x_0, i]
        else:
            i += 1
            return calRoot(poly, x_n, epsilon, i)

    return calRoot(poly, x_0, epsilon, i)

print(computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1, 0.0001))