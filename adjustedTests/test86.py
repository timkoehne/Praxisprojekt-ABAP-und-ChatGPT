def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate('Hi') == 'Hi'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('hello') == 'ehllo'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('number') == 'bemnru'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('abcd') == 'abcd'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('Hello World!!!') == 'Hello !!!Wdlor'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('') == ''
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('Hi. My name is Mister Robot. How are you?') == '.Hi My aemn is Meirst .Rboot How aer ?ouy'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    # Check some edge cases that are easy to work out by hand.

    return passed, failed
