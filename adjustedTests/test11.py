

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('111000', '101010') == '010010'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('1', '1') == '0'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('0101', '0000') == '0101'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
