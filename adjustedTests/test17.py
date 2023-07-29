

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('') == []
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('o o o o') == [4, 4, 4, 4]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('.| .| .| .|') == [1, 1, 1, 1]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2]
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
