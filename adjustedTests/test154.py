def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases

    # Check some edge cases that are easy to work out by hand.
    try:
        assert  candidate("xyzw","xyw") == False , "test #0"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert  candidate("yello","ell") == True , "test #1"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert  candidate("whattup","ptut") == False , "test #2"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert  candidate("efef","fee") == True , "test #3"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert  candidate("abab","aabb") == False , "test #4"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert  candidate("winemtt","tinem") == True , "test #5"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
