

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('(()(())((())))') == [4]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
