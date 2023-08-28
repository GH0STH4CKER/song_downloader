#[+] Author : GH0STH4CK3R
#[+] (C) Copyright Protected

import gzip,zlib,marshal,base64
from colorama import Fore , init
init()
lg = Fore.LIGHTGREEN_EX    # Colours
ly = Fore.LIGHTYELLOW_EX
lr = Fore.LIGHTRED_EX

banner = """
  █▀ █▀█ █▄ █ █▀▀   █▀▄ █▀█ █ █ █ █▄ █ █   █▀█ ▄▀█ █▀▄
  ▄█ █▄█ █ ▀█ █▄█   █▄▀ █▄█ ▀▄▀▄▀ █ ▀█ █▄▄ █▄█ █▀█ █▄▀
--------------------------------------------------------"""
tag = """     [+] Made By GH0STH4CK3R       [+] Version 3.0
--------------------------------------------------------"""

print(lg + banner)
print(ly + tag)

exec(marshal.loads(gzip.decompress(zlib.decompress(base64.b64decode(b'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')))))
