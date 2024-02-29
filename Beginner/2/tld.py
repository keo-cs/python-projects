from dataclasses import dataclass
from pathlib import Path

import requests


@dataclass
class TLD_List:
    tld_list: list[str]

    def clean(self) -> list[str]:
        r = self.tld_list
        try:
            # rm empty strings
            r = [x for x in r if x]
            # rm comments
            r = [x for x in r if not x.startswith("#")]
        except Exception as e:
            print(e)
            pass

        try:
            # rm whitespace
            r = [x.strip().lower() for x in r]
        except Exception as e:
            print(e)
            pass

        try:
            # rm duplicates
            r = sorted(list(set(r)))
        except Exception as e:
            print(e)
            pass

        # return sorted list
        return r


def get_online_list() -> list[str]:
    r = requests.get("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")
    r = r.text.split("\n")

    return TLD_List(tld_list=r).clean()


def get_local_list(tld_list_path: str) -> list[str]:
    tld_list_path = Path(tld_list_path)

    with open(str(tld_list_path.absolute()), "r") as of:
        r = of.read().split(",")
        r = [x.strip("[]").strip().strip("'") for x in r]
        r = TLD_List(tld_list=r).clean()

    return r


def save_local_list(tld_list: list[str], save_path: str) -> None:
    save_path = Path(save_path)
    tld_list = TLD_List(tld_list)

    with open(str(save_path.absolute()), "w") as of:
        of.write(str(tld_list.clean()))
