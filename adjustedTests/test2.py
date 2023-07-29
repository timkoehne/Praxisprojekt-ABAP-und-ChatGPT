

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate(3.5) == 0.5
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert abs(candidate(1.33) - 0.33) < 1e-6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert abs(candidate(123.456) - 0.456) < 1e-6
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
