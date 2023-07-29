

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate([], 'john') == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['grunt', 'trumpet', 'prune', 'gruesome'], 'run') == ['grunt', 'prune']
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
