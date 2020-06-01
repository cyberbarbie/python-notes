import re

#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_num_regex.search('My number is 760-586-3618.')
print('Phone number found: ' + mo.group())

print(phone_num_regex)

# \d- in regex stands for a digital character
# checks for phone number pattern in string of numbers