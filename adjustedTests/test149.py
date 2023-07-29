def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(["aa", "a", "aaa"]) == ["aa"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(["d", "b", "c", "a"]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(["d", "dcba", "abcd", "a"]) == ["abcd", "dcba"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(["AI", "ai", "au"]) == ["AI", "ai", "au"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(["a", "b", "b", "c", "c", "a"]) == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['aaaa', 'bbbb', 'dd', 'cc']) == ["cc", "dd", "aaaa", "bbbb"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
