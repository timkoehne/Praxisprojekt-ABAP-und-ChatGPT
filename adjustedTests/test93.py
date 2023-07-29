def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    
    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
