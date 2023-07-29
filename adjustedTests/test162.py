def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('') == None
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('A B C') == '0ef78513b0cb8cef12743f5aeb35f888'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('password') == '5f4dcc3b5aa765d61d8327deb882cf99'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.

    return passed, failed
