from urllib.parse import urlparse

DOMAIN = "oldhost.ancientdomain.com"
REPLACE_DOMAIN = "newhost.moderndomain.com"

DO_SILENT = True


def echo(*args, **kwargs):
    if not DO_SILENT:
        print(*args, **kwargs)


def parse(url: str) -> urlparse:
    # Add protocol if not present.
    # - Required for urlparse to assign the correct netloc,
    #   which is how validation is performed.
    echo(f"Parsing URL: {url}")
    if not url.startswith("http"):
        echo(f"Adding protocol to URL: {url}")
        url = f"https://{url}"

    return urlparse(url)


def make_valid(url: str, replace_any_domain: bool = False) -> str:
    echo(f"Making valid URL: {url}")
    echo(f"Replace any domain: {replace_any_domain}")

    parsed = parse(url)

    echo(f"Netloc: {parsed.netloc}")

    if parsed.netloc == REPLACE_DOMAIN or replace_any_domain:
        echo(f"Replacing domain: {parsed.netloc} -> {DOMAIN}")
        parsed = parsed._replace(netloc=DOMAIN)
    else:
        echo(
            f"Not replacing domain (replace_any_domain={replace_any_domain}, netloc={parsed.netloc}, REPLACE_DOMAIN={REPLACE_DOMAIN})"
        )
        print(f"Invalid: {url}")
        return

    return parsed.geturl()


if __name__ == "__main__":

    while True:
        r = input("\nEnter a URL: ")
        if r == "exit":
            break

        r = make_valid(r)
        if r:
            print(r)
