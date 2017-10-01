# ^[a-zA-Z]{5,10}$

VALID_USERNAMES = (
    "a" * 5,
    "a" * 7,
    "a" * 10,
    "A" * 5,
    "A" * 10,
    "aA" * 3,
    "Abcde"
)

INVALID_USERNAMES = (
    "",
    "a",
    "aaaa",
    "_aaaa",
    "-aaaa",
    "1",
    "1111",
    "_1111",
    "-1111",
    "a" * 11,
    "1" * 11,
    "_" * 5,
    ":" * 5,
    "A",
    "A" * 4,
    "_AAAA",
    "-AAAA",
    "1aaaa",
    "aaaa1",
    "1" * 5,
    "1" * 10,
    "1AAAA",
    "AAAA1",
)
