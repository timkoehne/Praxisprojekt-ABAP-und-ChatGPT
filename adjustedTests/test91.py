def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("Hello world") == 0, "Test 1"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Is the sky blue?") == 0, "Test 2"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("I love It !") == 1, "Test 3"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("bIt") == 0, "Test 4"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("I feel good today. I will be productive. will kill It") == 2, "Test 5"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("You and I are going for a walk") == 0, "Test 6"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
