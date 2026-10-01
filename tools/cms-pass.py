#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Turn a password into the value CMS_PASSWORD_HASH wants.

Run it where the password is chosen, paste the one line it prints into Vercel,
and the password itself never travels: not through me, not through a chat, not
into a commit. Nobody who can read the environment variable can read the
password out of it either.

    python3 tools/cms-pass.py

It asks without echoing, twice, and prints

    scrypt$16384$<salt>$<hash>

N=16384 is the cost. A wrong guess costs about a tenth of a second here, which
is nothing for the one person signing in and a wall for anybody working through
a word list. api/cms.js reads N out of the string, so raising it later does not
invalidate what is already set.
"""

import getpass
import hashlib
import os
import sys

N = 16384


def main():
    first = getpass.getpass("New editor password: ")
    if len(first) < 12:
        sys.exit("Too short. Twelve characters or more -- this is the only "
                 "thing between the internet and the site's content.")
    if first != getpass.getpass("Again: "):
        sys.exit("They did not match. Nothing written.")
    salt = os.urandom(16)
    digest = hashlib.scrypt(first.encode("utf-8"), salt=salt, n=N, r=8, p=1,
                            dklen=32, maxmem=128 * N * 8 * 2)
    print()
    print("Set this as CMS_PASSWORD_HASH in Vercel (Project -> Settings ->")
    print("Environment Variables), for Production and Preview:")
    print()
    print("scrypt$%d$%s$%s" % (N, salt.hex(), digest.hex()))
    print()
    print("Two more are needed, and neither of them is this one:")
    print("  CMS_SESSION_SECRET  -- run: openssl rand -hex 32")
    print("  GITHUB_TOKEN        -- a fine-grained token, Contents: read and")
    print("                         write, on this repository only")


if __name__ == "__main__":
    main()
