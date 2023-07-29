def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("a") == False , "a"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("aa") == False , "aa"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("abcd") == True , "abcd"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("aabb") == False , "aabb"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("adb") == True , "adb"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("xyy") == False , "xyy"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("iopaxpoi") == True , "iopaxpoi"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("iopaxioi") == False , "iopaxioi"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
