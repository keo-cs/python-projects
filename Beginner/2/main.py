import argparse
from urllib.parse import urlparse
import tldextract


def parse(url: str) -> urlparse:
    # Add protocol if not present.
    # - Required for urlparse to assign the correct netloc,
    #   which is how validation is performed.
    echo(f"Parsing URL: {url}")
    if not url.startswith("http"):
        echo(f"Adding protocol to URL: {url}")
        url = f"https://{url}"

    return urlparse(url)


def is_hash(value: str, required_length: int) -> bool:
    if len(value) != required_length:
        echo(f"Invalid hash: length={len(value)} (required={required_length})")
        return False
    if not value.alnum():
        echo("Invalid hash: contains non-alphanumeric characters")
        return False
    return True


def is_sha256(value) -> bool:
    return is_hash(value, 64)


def is_md5(value) -> bool:
    return is_hash(value, 32)


def is_ipv4(ip: str) -> bool:
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True


def is_domain(domain: str, failout: bool = False) -> bool:
    # Limit domain length to 64 characters for simplicity
    max_length = 64
    if len(domain) > max_length:

        return False

    parts = domain.split(".")

    # Domain should have at least 2 parts
    if len(parts) < 2:
        return False

    if is_ipv4(domain):
        return False

    def has_valid_tld(domain: str) -> bool:
        extracted = tldextract.extract(domain)
        return True if extracted.suffix else False

    if not has_valid_tld(domain):
        return False

    # Iterate through each domain fragment
    for part in parts:
        # Iterate through each character in the fragment
        for char in part:
            if not char.isalnum() and char != "-":
                return False

    return True


def is_url(url: str, do_nested_checks: bool = False) -> bool:
    if do_nested_checks:
        if is_domain(url):
            return False
        elif is_ipv4(url):
            return False
    return not is_domain(parse(url).netloc)


def get_ioc_type(
    value: str,
    allow_multiple_types: bool = False,
    allow_none: bool = False,
    allow_nested_checks: bool = False,
) -> str:
    r = []
    if "." in value or ":" in value:
        if "/" in value:
            if is_url(value, do_nested_checks=allow_nested_checks):
                r.append("URL")
        else:
            if is_domain(value):
                r.append("DOMAIN")
            if is_ipv4(value):
                r.append("IPv4")
            # if is_ipv6(value):
            #     r.append("IPv6")
    elif len(value) >= 32 and len(value) <= 64:
        if is_sha256(value):
            r.append("SHA256")
        if is_md5(value):
            r.append("MD5")
    else:
        if not allow_none:
            raise ValueError(f"Invalid IOC: {value}")

    if not r and not allow_none:
        raise ValueError(f"Invalid IOC: {value}")

    if len(r) > 1 and not allow_multiple_types:
        raise ValueError(f"Multiple types detected: {r}")

    return r[0]


def echo(*args, **kwargs):
    if not DO_SILENT:
        print(*args, **kwargs)


parser = argparse.ArgumentParser(
    prog="what_the.py",
    description="What the",
    epilog="What is it?",
)

parser.add_argument("value")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-n", "--allow_none", action="store_true")
parser.add_argument("-mA", "--allow_multiple", action="store_true")
parser.add_argument("-mC", "--nested_checks", action="store_true")

args = parser.parse_args()

DO_SILENT = not args.verbose

ioc = args.value

try:
    ioc_type = get_ioc_type(
        ioc,
        allow_nested_checks=args.nested_checks,
        allow_none=args.allow_none,
        allow_multiple_types=args.allow_multiple,
    )
    print(f"IOC Type(s): {ioc_type}")
except ValueError as e:
    print(f"Error: {e}")
    exit(1)
