def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("example.txt") == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("1example.dll") == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('s1sdf3.asd') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('K.dll') == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('MY16FILE3.exe') == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('His12FILE94.exe') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('_Y.txt') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('?aREYA.exe') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('/this_is_valid.dll') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('this_is_valid.wow') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('this_is_valid.txt') == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('this_is_valid.txtexe') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('#this2_i4s_5valid.ten') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('@this1_is6_valid.exe') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('this_is_12valid.6exe4.txt') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('all.exe.txt') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('I563_No.exe') == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('Is3youfault.txt') == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('no_one#knows.dll') == 'Yes'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('1I563_Yes3.exe') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('I563_Yes3.txtt') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('final..txt') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('final132') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('_f4indsartal132.') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    
        

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate('.txt') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('s.') == 'No'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
