def check(candidate):
    passed = 0
    failed = 0

    # Check some simple cases
    try:
        assert candidate('Watashi', ['tEN', 'niNE', 'eIGHt8OKe']) == 'Watashi.eIGHt8OKe'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('Boku123', ['nani', 'NazeDa', 'YEs.WeCaNe', '32145tggg']) == 'Boku123.YEs.WeCaNe'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('__YESIMHERE', ['t', 'eMptY', 'nothing', 'zeR00', 'NuLl__', '123NoooneB321']) == '__YESIMHERE.NuLl__'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('K', ['Ta', 'TAR', 't234An', 'cosSo']) == 'K.TAR'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('__HAHA', ['Tab', '123', '781345', '-_-']) == '__HAHA.123'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('YameRore', ['HhAas', 'okIWILL123', 'WorkOut', 'Fails', '-_-']) == 'YameRore.okIWILL123'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('finNNalLLly', ['Die', 'NowW', 'Wow', 'WoW']) == 'finNNalLLly.WoW'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1

    # Check some edge cases that are easy to work out by hand.
    try:
        assert candidate('_', ['Bb', '91245']) == '_.Bb'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    try:
        assert candidate('Sp', ['671235', 'Bb']) == 'Sp.671235'
        passed += 1
    except (AssertionError, TypeError):
        failed += 1
    
    return passed, failed
