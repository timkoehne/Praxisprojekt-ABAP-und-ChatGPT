def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(19) == 'xix'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(152) == 'clii'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(251) == 'ccli'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(426) == 'cdxxvi'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(500) == 'd'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1) == 'i'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(4) == 'iv'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(43) == 'xliii'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(90) == 'xc'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(94) == 'xciv'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(532) == 'dxxxii'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(900) == 'cm'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(994) == 'cmxciv'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(1000) == 'm'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
