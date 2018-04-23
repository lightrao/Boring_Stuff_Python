import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.') #If the pattern is found, the search() method returns a Match object.
print('Phone number found: ' + mo.group())
