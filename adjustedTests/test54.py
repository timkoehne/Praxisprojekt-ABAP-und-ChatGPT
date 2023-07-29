

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('abcd', 'dddddddabc') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('dddddddabc', 'abcd') == True
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('eabcd', 'dddddddabc') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('abcd', 'dddddddabcf') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('aabb', 'aaccc') == False
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
