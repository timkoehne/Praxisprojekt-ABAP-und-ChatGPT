def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate('Hello') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('abcdcba') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('kittens') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('orange') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('wow') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('world') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('MadaM') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('Wow') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('HI') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('go') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('gogo') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('aaaaaaaaaaaaaaa') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate('Madam') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('M') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('0') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
