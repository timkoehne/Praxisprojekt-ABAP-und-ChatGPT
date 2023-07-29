

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    passed = 0
    failed = 0
    try:
        assert candidate('') == ''
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('three') == 'three'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('three five nine') == 'three five nine'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('six five four three two one zero') == 'zero one two three four five six'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
