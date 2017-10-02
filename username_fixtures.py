# ^[a-zA-Z]{5,10}$

VALID_USERNAMES = (
    ("Test method 'list' with valid 'name' with minimal boundary value of length and symbols in lower case", "a" * 5),
    ("Test method 'list' with valid 'name' with length in range and symbols in lower case", "a" * 7),
    ("Test method 'list' with valid 'name' with minimal boundary value of length and symbols in upper case", "A" * 5),
    ("Test method 'list' with valid 'name' with length in range and symbols in upper case", "A" * 8),
    ("Test method 'list' with valid 'name' with maximal boundary value of length and symbols in lower and upper case",
     "Bb" * 5),
)

INVALID_USERNAMES = (
    ("Test method 'list' with invalid 'name' - empty value", ""),
    ("Test method 'list' with invalid 'name' - short value in lower case", "a"),
    ("Test method 'list' with invalid 'name' - short digital value", "1"),
    ("Test method 'list' with invalid 'name' - short value in upper case", "A"),
    ("Test method 'list' with invalid 'name' - boundary short value in lower case", "aaaa"),
    ("Test method 'list' with invalid 'name' - boundary short value in upper case", "A" * 4),
    ("Test method 'list' with invalid 'name' - boundary short digital value", "1111"),
    ("Test method 'list' with invalid 'name' - empty value", "_1111"),
    ("Test method 'list' with invalid 'name' - empty value", "-1111"),
    ("Test method 'list' with invalid 'name' - boundary long value in lower case", "d" * 11),
    ("Test method 'list' with invalid 'name' - boundary long value in upper case", "D" * 11),
    ("Test method 'list' with invalid 'name' - boundary long digital value", "1" * 11),
    ("Test method 'list' with invalid 'name' - underscore symbols only", "_" * 5),
    ("Test method 'list' with invalid 'name' - minus symbols only", "-" * 5),
    ("Test method 'list' with invalid 'name' - digit and letters", "1aaaa"),
    ("Test method 'list' with invalid 'name' - special symbol '_' with correct length", "_" * 5),
    ("Test method 'list' with invalid 'name' - digital value with minimal correct length", "1" * 5),
    ("Test method 'list' with invalid 'name' - digital value with maximum correct length", "1" * 10),
    ("Test method 'list' with invalid 'name' - value with special symbol '_'", "_bbbb"),
    ("Test method 'list' with invalid 'name' - value with special symbol '.'", ".kkkk"),
    ("Test method 'list' with invalid 'name' - value with special symbol ','", ",kkkk"),
    ("Test method 'list' with invalid 'name' - value with special symbol '/'", "/kkkk"),
    ("Test method 'list' with invalid 'name' - value with special symbol '^'", "^kkkk"),
    ("Test method 'list' with invalid 'name' - value with special symbol '%'", "%kkkk"),
    ("Test method 'list' with invalid 'name' - value with special symbol '-'", "-kkkk"),
    ("Test method 'list' with invalid 'name': very big value", "z" * 9999),

)
