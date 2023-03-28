# -*- coding: utf-8 -*-
# Author : Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 09 February 2023

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