

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    import random

    try:
        assert candidate(0, 1) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1, 0) == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2, 3) == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5, 7) == 12
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7, 5) == 12
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    for i in range(100):
        x, y = random.randint(0, 1000), random.randint(0, 1000)
        try:
            assert candidate(x, y) == x + y
            passed += 1
        except (AssertionError, TypeError):
            failed += 1

    return passed, failed
