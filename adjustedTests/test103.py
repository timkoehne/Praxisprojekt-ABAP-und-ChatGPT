def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate(1, 5) == "0b11"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(7, 13) == "0b1010"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(964,977) == "0b1111001010"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(996,997) == "0b1111100100"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(560,851) == "0b1011000010"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(185,546) == "0b101101110"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(362,496) == "0b110101101"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(350,902) == "0b1001110010"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(197,233) == "0b11010111"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate(7, 5) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5, 1) == -1
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate(5, 5) == "0b101"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
