#! python3
# strings.py

import sys
import pyperclip

"""
Copies password of your account so you can paste to log in.
"""
passwords = {
    'twitter': "1234555666",
    "facebook": "2677833939",

}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print(f'Password for {account} has been copied')
else:
    print(f'There is no account named {account}')






