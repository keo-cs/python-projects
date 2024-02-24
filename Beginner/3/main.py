from urllib.parse import urlparse
import argparse


def echo(*args, **kwargs):
    if not DO_SILENT:
        print(*args, **kwargs)


def defang(url):
    parsed_url = urlparse(url)
    defanged_hostname = parsed_url.hostname.replace(".", "[.]")
    defanged_url = f"{parsed_url.scheme}://{defanged_hostname}{parsed_url.path}"
    if parsed_url.query:
        defanged_url += f"?{parsed_url.query}"
    if parsed_url.fragment:
        defanged_url += f"#{parsed_url.fragment}"
    return defanged_url


parser = argparse.ArgumentParser(
    prog="d_fang.py",
    description="Defang a URL",
)

parser.add_argument("url")
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()

DO_SILENT = not args.verbose


url = "https://host.domain.com/path/?key=val#id"
df = defang(url)

echo("Original URL:", url)
echo("Defanged URL:", df)
