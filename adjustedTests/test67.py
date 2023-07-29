def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("5 apples and 6 oranges",19) == 8
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("5 apples and 6 oranges",21) == 10
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("0 apples and 1 oranges",3) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1 apples and 0 oranges",3) == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("2 apples and 3 oranges",100) == 95
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("2 apples and 3 oranges",5) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1 apples and 100 oranges",120) == 19
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
