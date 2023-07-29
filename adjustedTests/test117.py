def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("Mary had a little lamb", 4) == ["little"], "First test error: " + str(candidate("Mary had a little lamb", 4))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Mary had a little lamb", 3) == ["Mary", "lamb"], "Second test error: " + str(candidate("Mary had a little lamb", 3))  
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("simple white space", 2) == [], "Third test error: " + str(candidate("simple white space", 2))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Hello world", 4) == ["world"], "Fourth test error: " + str(candidate("Hello world", 4))  
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Uncle sam", 3) == ["Uncle"], "Fifth test error: " + str(candidate("Uncle sam", 3))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate("", 4) == [], "1st edge test error: " + str(candidate("", 4))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("a b c d e f", 1) == ["b", "c", "d", "f"], "2nd edge test error: " + str(candidate("a b c d e f", 1))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
