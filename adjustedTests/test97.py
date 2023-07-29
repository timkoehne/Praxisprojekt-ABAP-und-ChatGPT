def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(148, 412) == 16, "First test error: " + str(candidate(148, 412))                    
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(19, 28) == 72, "Second test error: " + str(candidate(19, 28))           
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(2020, 1851) == 0, "Third test error: " + str(candidate(2020, 1851))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(14,-15) == 20, "Fourth test error: " + str(candidate(14,-15))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(76, 67) == 42, "Fifth test error: " + str(candidate(76, 67))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(17, 27) == 49, "Sixth test error: " + str(candidate(17, 27))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(0, 1) == 0, "1st edge test error: " + str(candidate(0, 1))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(0, 0) == 0, "2nd edge test error: " + str(candidate(0, 0))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
