def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([152, 323, 1422, 10]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([12345, 2033, 111, 151]) == [111, 151]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([135, 103, 31]) == [31, 135]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
