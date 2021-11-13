#!/usr/bin/python3

#Simple test values
#Missing Mail Innovations test

import py_tracking_urls

errors = False

numbers = {
	#TEST UPS
	'1Z9999W99999999999'			: 'ups.com',
	'1Z12345E1512345676'			: 'ups.com',
	'1Z12345E0205271688'			: 'ups.com',
	'1Z12345E6605272234'			: 'ups.com',
	'1Z12345E0305271640'			: 'ups.com',
	'1Z12345E0393657226'			: 'ups.com',
	'1Z12345E1305277940'			: 'ups.com',
	'1Z12345E6205277936'			: 'ups.com',
	'1Z12345E1505270452'			: 'ups.com',
	'1Z648616E192760718'			: 'ups.com',
	'1ZWX0692YP40636269'			: 'ups.com',
	'T9999999999'					: 'ups.com',
	#TEST FEDEX
	'9999 9999 9999'				: 'fedex.com',
	'9999 9999 9999 999'			: 'fedex.com',
	'999999999999'					: 'fedex.com',
	'999999999999999'				: 'fedex.com',
	'661377569221'					: 'fedex.com',
	'624893691092'					: 'fedex.com',
	'61299995669352455464'			: 'fedex.com',
	'61299995669151880177'			: 'fedex.com',
	'00408017007469'				: 'fedex.com',
	#TEST USPS
	'9400 1000 0000 0000 0000 00'	: 'usps.com',
	'9205 5000 0000 0000 0000 00'	: 'usps.com',
	'9407 3000 0000 0000 0000 00'	: 'usps.com',
	'9303 3000 0000 0000 0000 00'	: 'usps.com',
	'82 000 000 00'					: 'usps.com',
	'EC 000 000 000 US'				: 'usps.com',
	'9270 1000 0000 0000 0000 00'	: 'usps.com',
	'EA 000 000 000 US'				: 'usps.com',
	'CP 000 000 000 US'				: 'usps.com',
	'9208 8000 0000 0000 0000 00'	: 'usps.com',
	'9202 1000 0000 0000 0000 00'	: 'usps.com',
	'9400100000000000000000'		: 'usps.com',
	'9205500000000000000000'		: 'usps.com',
	'9407300000000000000000'		: 'usps.com',
	'9303300000000000000000'		: 'usps.com',
	'8200000000'					: 'usps.com',
	'EC000000000US'					: 'usps.com',
	'9270100000000000000000'		: 'usps.com',
	'EA000000000US'					: 'usps.com',
	'CP000000000US'					: 'usps.com',
	'9208800000000000000000'		: 'usps.com',
	'9202100000000000000000'		: 'usps.com',
	'92748963438592543475924253'	: 'usps.com',
	#TEST ONTRAC
	'C00000000000000'				: 'ontrac.com',
	'C99999999999999'				: 'ontrac.com',
	#TEST DHL
	'125-12345678'					: 'dhl.com',
	'125 12345678'					: 'dhl.com',
	'12512345678'					: 'dhl.com',
	'SEA1234567'					: 'dhl.com',
	'LAX1234567'					: 'dhl.com',
    #TEST DHL GLOBAL
    '4041005861941412'              : 'dhlglobalmail.com',
    #Royal Mail
    'AB123456789GB'                 : 'royalmail.com',
	#INVALID TRACKING NUMBERS
	'INVALID TRACKING NUMBER'		: False
}

for number, service in numbers.items():
	print('TESTING: ' + number)
	url = py_tracking_urls.get_tracking_url(number)
	if url:
		print(url)
		if service not in url:
			print(" ---  FAILED  ---  WRONG SERVICE DETECTED  ---")
			errors = True
	else:
		if not url and not service:
			print(" ---  NO SERVICE AVAILABLE FOR THIS VALUE  ---")
		else:
			print(" ---  FAILED  ---  NO SERVICE FOUND  ---")
			errors = True;
	print(" ")

if errors:
	print(" --- ERROR FOUND  ---  TEST FAILED  ---")
	exit(1);
else:
	print(" !!! ALL GOOD !!!")
