#! python3
# strings.py

import sys
import pyperclip

passwords = {
    'twitter': "1Plus2is3",
    "facebook": "TheLordisgood"

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






