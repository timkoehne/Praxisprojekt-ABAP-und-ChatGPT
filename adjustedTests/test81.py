def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1.2]) == ['D+']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([0.5]) == ['D-']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([0.0]) == ['E']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([0, 0.7]) == ['E', 'D-']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
