#!/usr/bin/env python3

from checkuser1 import checkUser
import sys
email = sys.argv[1]
mail = checkUser(email)
print(mail)
