def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("") == 0, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("abAB") == 131, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("abcCd") == 67, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("helloE") == 69, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("woArBld") == 131, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("aAaaaXa") == 153, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(" How are yOu?") == 151, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("You arE Very Smart") == 327, "Error"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
