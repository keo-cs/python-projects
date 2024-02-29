import argparse
import secrets
import string


def echo(*args, **kwargs):
    if not DO_SILENT:
        print(*args, **kwargs)


def generate(
    length,
    use_lowercase=True,
    use_uppercase=True,
    use_digits=True,
    use_special_chars=True,
):
    """
    Generate a password based on specified criteria.

    Args:
    - length: Required length of the password
    - use_lowercase: Boolean indicating whether to include lowercase characters
    - use_uppercase: Boolean indicating whether to include uppercase characters
    - use_digits: Boolean indicating whether to include digits
    - use_special_chars: Boolean indicating whether to include special characters

    Returns:
    - Password string meeting the specified criteria
    """
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type should be included")

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


parser = argparse.ArgumentParser(
    prog="gimme_pw.py",
    description="Generate a password",
)

parser.add_argument("length", type=int)
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-l", "--no_lowercase", action="store_true")
parser.add_argument("-u", "--no_uppercase", action="store_true")
parser.add_argument("-d", "--no_digits", action="store_true")
parser.add_argument("-s", "--no_special", action="store_true")

args = parser.parse_args()

DO_SILENT = not args.verbose


pw = generate(
    length=args.length,
    use_lowercase=not args.no_lowercase,
    use_uppercase=not args.no_uppercase,
    use_digits=not args.no_digits,
    use_special_chars=not args.no_special,
)

print(pw)
