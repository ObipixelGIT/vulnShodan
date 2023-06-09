# vulnShodan
Discover vulnerable systems and/or services on Shodan for your security footprinting/reconnaissance and OSINT requirements.

## How this script works?
- Uses an API Key from Shodan.io and searches for vulnerable servers and/or services from the terminal.

## Preparation
- Go to Shodan.io and Register an account.
- Login to your Shodan.io account.
- Issue/Create an API Key.
- Copy the API key into the script (replace: YOURAPIKEYGOESHERE with your API Key).
- Change what you are searching for (replace: YOURSEARCHGOESHERE with your search e.g. SQL).

<br>

- Install the Shodan.io libary:
```bash
pip3 install optparse
```

## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x vulnShodan.py
```

## Usage
```bash
sudo python3 vulnShodan.py
```

## Example script
```python
#/usr/bin/python3

import shodan

SHODAN_API_KEY = 'YOURAPIKEYGOESHERE'

api = shodan.Shodan(SHODAN_API_KEY)

try:
	# Search Shodan
	results = api.search('YOURSEARCHGOESHERE')

	# Show the results
	for result in results['matches']:
		print ('%s' % result['ip_str'])
		#print ('=====================')
		print (result['data'])
		print ('=====================')
except shodan.APIError:
	print ('Error: %s' % e)
```

## Disclaimer
"The scripts in this repository are intended for authorized security testing and/or educational purposes only. Unauthorized access to computer systems or networks is illegal. These scripts are provided "AS IS," without warranty of any kind. The authors of these scripts shall not be held liable for any damages arising from the use of this code. Use of these scripts for any malicious or illegal activities is strictly prohibited. The authors of these scripts assume no liability for any misuse of these scripts by third parties. By using these scripts, you agree to these terms and conditions."

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.
