def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate([], []) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['4'], ['1', '2', '3', '4', '5']) == ['4']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate([], ['this']) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['this'], []) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
