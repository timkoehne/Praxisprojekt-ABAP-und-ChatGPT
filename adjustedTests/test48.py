

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('aba') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('aaaaa') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('zbcd') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('xywyx') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('xywyz') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('xywzx') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
