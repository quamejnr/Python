import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
bat
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://www.knust.edu.gh
https://www.alibaba.com
'''
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w.+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match.group())
subbed = pattern.sub(r'\2\3', urls)
# print(subbed)

# for match in matches:
#     print(f'{match.group(2)}{match.group(3)}')

# with open('text2.txt', 'w') as f:
#     f.write(subbed)
