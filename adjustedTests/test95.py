def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate({"p":"pineapple", "b":"banana"}) == True, "First test error: " + str(candidate({"p":"pineapple", "b":"banana"}))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate({"p":"pineapple", "A":"banana", "B":"banana"}) == False, "Second test error: " + str(candidate({"p":"pineapple", "A":"banana", "B":"banana"}))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate({"p":"pineapple", 5:"banana", "a":"apple"}) == False, "Third test error: " + str(candidate({"p":"pineapple", 5:"banana", "a":"apple"}))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate({"Name":"John", "Age":"36", "City":"Houston"}) == False, "Fourth test error: " + str(candidate({"Name":"John", "Age":"36", "City":"Houston"}))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate({"STATE":"NC", "ZIP":"12345" }) == True, "Fifth test error: " + str(candidate({"STATE":"NC", "ZIP":"12345" }))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate({"fruit":"Orange", "taste":"Sweet" }) == True, "Fourth test error: " + str(candidate({"fruit":"Orange", "taste":"Sweet" }))      
        passed += 1
    except (AssertionError, TypeError):
        failed += 1


    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate({}) == False, "1st edge test error: " + str(candidate({}))
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    return passed, failed
