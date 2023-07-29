

METADATA = {}
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def check(candidate):
    passed = 0
    failed = 0
    from random import randint, choice
    import copy
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_shift(str)
        try:
            assert candidate(copy.deepcopy(encoded_str)) == str
            passed += 1
        except (AssertionError, TypeError):
            failed += 1

    return passed, failed
