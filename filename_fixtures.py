# ^[^.][a-z0-9.]{1,15}$

VALID_FILENAMES = (
    ("Test method 'create' with valid 'filename' with minimal length", "ab"),
    ("Test method 'create' with valid 'filename' with minimal length and 'dot' symbol", "a."),
    ("Test method 'create' with valid 'filename' with minimal length and digit", "a1"),
    ("Test method 'create' with valid 'filename' with digits only", "42"),
    ("Test method 'create' with valid 'filename' with upper case letter on first place", "File.txt"),
    ("Test method 'create' with valid 'filename' with maximal length", "m" * 16),
    ("Test method 'create' with valid 'filename' with maximal length and digits only", "1" * 16),
    ("Test method 'create' with valid 'filename' with length in range mixed letters, digits, dots", "File.12345.xlsx"),
)

INVALID_FILENAMES = (
    ("Test method 'create' with invalid 'filename': empty value", ""),
    ("Test method 'create' with invalid 'filename': short length", "x"),
    ("Test method 'create' with invalid 'filename': started from dot", ".o"),
    ("Test method 'create' with invalid 'filename': too long", "f" * 17),
    ("Test method 'create' with invalid 'filename': has character in uppercase not in beginning", "fFf"),
    ("Test method 'create' with invalid 'filename': has space in the middle of a word ", "ss ss"),
    ("Test method 'create' with invalid 'filename': has special symbol ',' in the middle of a word ", "sss,zzz"),
    ("Test method 'create' with invalid 'filename': has special symbol '/' in the middle of a word ", "sss/zzz"),
    ("Test method 'create' with invalid 'filename': has special symbol '-' in the middle of a word ", "sss-zzz"),
    ("Test method 'create' with invalid 'filename': has special symbol '_' in the middle of a word ", "sss_zzz"),
    ("Test method 'create' with invalid 'filename': has special symbol '^' in the middle of a word ", "sss^zzz"),
    ("Test method 'create' with invalid 'filename': has special symbol '&' in the middle of a word ", "sss&zzz"),
    ("Test method 'create' with invalid 'filename': has special symbol '@' in the middle of a word ", "sss@zzz"),
    ("Test method 'create' with invalid 'filename': has special symbol '#' in the middle of a word ", "sss#zzz"),
    ("Test method 'create' with invalid 'filename': has special symbol '=' in the middle of a word ", "sss=zzz"),
    ("Test method 'create' with invalid 'filename': has special symbol '+' in the middle of a word ", "sss+zzz"),
    ("Test method 'create' with invalid 'filename': very big value", "z" * 9999),

)
