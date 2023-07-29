def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert (candidate(["name", "of", "string"]) == "string"), "t1"
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert (candidate(["name", "enam", "game"]) == "enam"), 't2'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert (candidate(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"), 't3'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert (candidate(["abc", "cba"]) == "abc"), 't4'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert (candidate(["play", "this", "game", "of","footbott"]) == "footbott"), 't5'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert (candidate(["we", "are", "gonna", "rock"]) == "gonna"), 't6'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert (candidate(["we", "are", "a", "mad", "nation"]) == "nation"), 't7'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert (candidate(["this", "is", "a", "prrk"]) == "this"), 't8'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert (candidate(["b"]) == "b"), 't9'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert (candidate(["play", "play", "play"]) == "play"), 't10'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
