def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("apple") == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("apple pi e") == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("eeeee") == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("A") == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Pumpkin pie ") == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Pumpkin pie 1") == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("") == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("eeeee e ") == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("apple pie") == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("apple pi e ") == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
