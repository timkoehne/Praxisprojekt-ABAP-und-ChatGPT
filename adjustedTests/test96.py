def check(candidate):
    passed = 0
    failed = 0

    try:
        assert candidate(5) == [2,3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(6) == [2,3,5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7) == [2,3,5]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(10) == [2,3,5,7]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(0) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(22) == [2,3,5,7,11,13,17,19]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(18) == [2,3,5,7,11,13,17]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(47) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
