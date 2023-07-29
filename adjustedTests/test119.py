def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(['()(', ')']) == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([')', ')']) == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['(()(())', '())())']) == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([')())', '(()()(']) == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['(())))', '(()())((']) == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['()', '())']) == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['(()(', '()))()']) == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(['((((', '((())']) == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([')(()', '(()(']) == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([')(', ')(']) == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(['(', ')']) == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate([')', '(']) == 'Yes' 
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
