def check(candidate):
    passed = 0
    failed = 0

    try:
        assert candidate("Hello world!") == ["Hello","world!"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Hello,world!") == ["Hello","world!"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Hello world,!") == ["Hello","world,!"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Hello,Hello,world !") == ["Hello,Hello,world","!"]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("abcdef") == 3
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("aaabb") == 2
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("aaaBb") == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("") == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
