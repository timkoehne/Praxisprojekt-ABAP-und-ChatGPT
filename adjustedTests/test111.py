def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate('a b b a') == {'a':2,'b': 2}, "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('a b c a b') == {'a': 2, 'b': 2}, "This prints if this assert fails 2 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, "This prints if this assert fails 3 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}, "This prints if this assert fails 4 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('b b b b a') == {'b': 4}, "This prints if this assert fails 5 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}, "This prints if this assert fails 6 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    
    
    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate('') == {}, "This prints if this assert fails 7 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('a') == {'a': 1}, "This prints if this assert fails 8 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
