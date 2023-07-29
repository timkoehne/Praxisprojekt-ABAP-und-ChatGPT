def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate('[[]]') == True, "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[]]]]]]][[[[[]') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[][]') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(('[]')) == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[[[[]]]]') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[]]]]]]]]]]') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[][][[]]') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[[]') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[]]') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[[]][[') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[[][]]') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate('') == False, "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('[[[[[[[[') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(']]]]]]]]') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
