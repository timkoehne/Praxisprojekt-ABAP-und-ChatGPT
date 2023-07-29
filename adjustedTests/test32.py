

METADATA = {}



def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    import math
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def check(candidate):
    passed = 0
    failed = 0
    import math
    import random
    rng = random.Random(42)
    import copy
    for _ in range(100):
        ncoeff = 2 * rng.randint(1, 4)
        coeffs = []
        for _ in range(ncoeff):
            coeff = rng.randint(-10, 10)
            if coeff == 0:
                coeff = 1
            coeffs.append(coeff)
        solution = candidate(copy.deepcopy(coeffs))
        try:
            assert math.fabs(poly(coeffs, solution)) < 1e-4
            passed += 1
        except (AssertionError, TypeError):
            failed += 1

    return passed, failed
