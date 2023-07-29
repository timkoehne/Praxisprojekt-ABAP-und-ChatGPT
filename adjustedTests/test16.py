

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('') == 0
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('abcde') == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('abcde' + 'cade' + 'CADE') == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('aaaaAAAAaaaa') == 1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('Jerry jERRY JeRRRY') == 5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
