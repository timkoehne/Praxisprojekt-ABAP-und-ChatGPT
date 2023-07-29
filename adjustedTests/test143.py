def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("This is a test") == "is"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("lets go for swimming") == "go for"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("there is no place available here") == "there is no place"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Hi I am Hussein") == "Hi am Hussein"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("go for it") == "go for it"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate("here") == ""
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("here is") == "is"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
