def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("AsDf") == "aSdF"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1234") == "4321"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("ab") == "AB"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("#a@C") == "#A@c"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("#AsdfW^45") == "#aSDFw^45"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("#6@2") == "2@6#"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate("#$a^D") == "#$A^d"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("#ccc") == "#CCC"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Don't remove this line:
    return passed, failed
