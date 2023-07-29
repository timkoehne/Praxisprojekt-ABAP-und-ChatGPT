def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("1/5", "5/1") == True, 'test1'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1/6", "2/1") == False, 'test2'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("5/1", "3/1") == True, 'test3'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("7/10", "10/2") == False, 'test4'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("2/10", "50/10") == True, 'test5'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("7/2", "4/2") == True, 'test6'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("11/6", "6/1") == True, 'test7'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("2/3", "5/2") == False, 'test8'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("5/2", "3/5") == False, 'test9'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("2/4", "8/4") == True, 'test10'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate("2/4", "4/2") == True, 'test11'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1/5", "5/1") == True, 'test12'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1/5", "1/5") == False, 'test13'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
