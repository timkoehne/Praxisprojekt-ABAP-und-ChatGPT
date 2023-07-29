def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate("Jupiter", "Neptune") == ("Saturn", "Uranus"), "First test error: " + str(len(candidate("Jupiter", "Neptune")))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Earth", "Mercury") == ("Venus",), "Second test error: " + str(candidate("Earth", "Mercury"))  
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Third test error: " + str(candidate("Mercury", "Uranus"))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus"), "Fourth test error: " + str(candidate("Neptune", "Venus"))  
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate("Earth", "Earth") == ()
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Mars", "Earth") == ()
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate("Jupiter", "Makemake") == ()
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
