def check(candidate):
    passed = 0
    failed = 0

    try:
        assert candidate("abcde","ae") == ('bcd',False)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("abcdef", "b") == ('acdef',False)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("abcdedcba","ab") == ('cdedc',True)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("dwik","w") == ('dik',False)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("a","a") == ('',True)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("abcdedcba","") == ('abcdedcba',True)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("abcdedcba","v") == ('abcdedcba',True)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("vabba","v") == ('abba',True)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("mamma", "mia") == ("", True)
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
