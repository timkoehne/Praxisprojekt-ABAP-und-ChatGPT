

METADATA = {}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('') == ''
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('fedcba') == 'fdcb'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('eeeee') == ''
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('acBAA') == 'cB'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('EcBOO') == 'cB'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('ybcd') == 'ybcd'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
