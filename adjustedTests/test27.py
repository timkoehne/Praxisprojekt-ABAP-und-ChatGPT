

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
        assert candidate('Hello!') == 'hELLO!'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    return passed, failed
