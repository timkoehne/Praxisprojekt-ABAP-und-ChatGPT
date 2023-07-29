

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('(()(())((())))') == ['(()(())((())))']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
