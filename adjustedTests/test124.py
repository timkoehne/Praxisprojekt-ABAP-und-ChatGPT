def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate('03-11-2000') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('15-01-2012') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('04-0-2040') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('06-04-2020') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('01-01-2007') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('03-32-2011') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('04-31-3000') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('06-06-2005') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('21-31-2000') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('04-12-2003') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('04122003') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('20030412') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('2003-04') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('2003-04-12') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    try:
        assert candidate('04-2003') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
