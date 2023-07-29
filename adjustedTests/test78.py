def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("AB") == 1, "First test error: " + str(candidate("AB"))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1077E") == 2, "Second test error: " + str(candidate("1077E"))  
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("ABED1A33") == 4, "Third test error: " + str(candidate("ABED1A33"))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("2020") == 2, "Fourth test error: " + str(candidate("2020"))  
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("123456789ABCDEF0") == 6, "Fifth test error: " + str(candidate("123456789ABCDEF0"))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("112233445566778899AABBCCDDEEFF00") == 12, "Sixth test error: " + str(candidate("112233445566778899AABBCCDDEEFF00"))  
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([]) == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
