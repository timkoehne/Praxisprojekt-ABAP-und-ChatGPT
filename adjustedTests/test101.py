def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Hi, my name") == ["Hi", "my", "name"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate("") == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("ahmed     , gamal") == ["ahmed", "gamal"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
