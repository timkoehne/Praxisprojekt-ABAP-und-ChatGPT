def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("yogurt") == "u"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("full") == "u"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("easy") == ""
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("eAsy") == ""
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("ali") == ""
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("bad") == "a"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("most") == "o"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("ab") == ""
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("ba") == ""
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("quick") == ""
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("anime") == "i"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Asia") == ""
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Above") == "o"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
