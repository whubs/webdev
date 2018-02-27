# /usr/bin/python

# A simple database

#  A dictionary with person names as keys. Each person is represented as
# another dictionary with the keys 'phone' and 'addr' referring to their phone
# numbers and addresses, respectively.

people = {

	'Alice': {
		'phone': '2341',
		'addr': 'Foo drive 23'
	},

	'Beth': {
		'phone': '9102',
		'addr': 'Bar street 42'
	},

	'Cecil': {
		'phone': '3158',
		'addr': 'Baz avenue 90'
	}
}

# Descriptive labels for the phone number and address. These will be used
# when printing the output.

labels = {
	'phone': 'phone number',
	'addr': 'address'
}

name = raw_input('Name: ');

# Are we looking for a phone number or an address?
request = raw_input('Phone number(p) or address(a)? ');

# Use correct key:
if request == 'p': key = 'phone';
if request == 'a': key = 'addr';

# Only try to print information if the name is a valid key in
# our dictionary:
if name in people: print "%s's %s is %s" % (name, labels[key], people[name][key]);