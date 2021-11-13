#!/usr/bin/env python3

#Module: py_tracking_urls
#Based on php-tracking-urls: https://github.com/darkain/php-tracking-urls
#With simple service name addtions: https://github.com/mgtremaine/php-tracking-urls
#
#Usage: url = py_tracking_urls.get_tracking_url(number)
#

import re
import urllib.parse

def get_tracking_url(tracking_number):
        if not tracking_number:
             return false
        if not isinstance(tracking_number, int) and not isinstance(tracking_number, str):
             return false

        tracking_urls = [
		#UPS - UNITED PARCEL SERVICE
		{
			'url': 'http://wwwapps.ups.com/WebTracking/processInputRequest?TypeOfInquiryNumber=T&InquiryNumber1=',
			'reg':r'\b(1Z ?[0-9A-Z]{3} ?[0-9A-Z]{3} ?[0-9A-Z]{2} ?[0-9A-Z]{4} ?[0-9A-Z]{3} ?[0-9A-Z]|T\d{3} ?\d{4} ?\d{3})\b'
		},
		#USPS - UNITED STATES POSTAL SERVICE - FORMAT 1 /^E\D{1}\d{9}\D{2}$|^9\d{15,21}$/
		{
			'url':'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=',
			'reg':r'\b((420 ?\d{5} ?)?(91|92|93|94|01|03|04|70|23|13)\d{2} ?\d{4} ?\d{4} ?\d{4} ?\d{4}( ?\d{2,6})?)\b'
		},
		#USPS - UNITED STATES POSTAL SERVICE - FORMAT 2
		{
			'url':'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=',
			'reg':r'\b((M|P[A-Z]?|D[C-Z]|LK|E[A-C]|V[A-Z]|R[A-Z]|CP|CJ|LC|LJ) ?\d{3} ?\d{3} ?\d{3} ?[A-Z]?[A-Z]?)\b'
		},
		#USPS - UNITED STATES POSTAL SERVICE - FORMAT 3
		{
			'url':'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=',
			'reg':r'\b(82 ?\d{3} ?\d{3} ?\d{2})\b'
		},
		#USPS - UNITED STATES POSTAL SERVICE - FORMAT 4
		{
			'url':'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=',
			'reg':r'\b(95\d{17})\b'
		},
		#Mail Innovations - UPS/UNITED STATES POSTAL SERVICE - FORMAT 1
		{
			'url':'http://wwwapps.ups.com/WebTracking/processInputRequest?TypeOfInquiryNumber=T&InquiryNumber1=',
			'reg':r'/\b(\d{18})\b'
		},
		#FEDEX - FEDERAL EXPRESS
		{
			'url':'http://www.fedex.com/Tracking?language=english&cntry_code=us&tracknumbers=',
            'reg':r'\b(((96\d\d|6\d)\d{3} ?\d{4}|96\d{2}|\d{4}) ?\d{4} ?\d{4}( ?\d{3}| ?\d{15})?)\b'
		},
		#ONTRAC
		{
			'url':'http://www.ontrac.com/trackres.asp?tracking_number=',
			'reg':r'\b(C\d{14})\b'
		},
		#DHL
		{
			'url':'http://www.dhl.com/content/g0/en/express/tracking.shtml?brand=DHL&AWB=',
			'reg':r'\b(\d{4}[- ]?\d{4}[- ]?\d{2}|\d{3}[- ]?\d{8}|[A-Z]{3}\d{7})\b'
		},
		#DHL eCommerce
		{
			'url':'https://webtrack.dhlglobalmail.com/?trackingnumber=',
			'reg':r'\b(\d{16}|\d{22})\b'
		},
		#Royal Mail
		{
			'url':'http://track2.royalmail.com/portal/rm/track?trackNumber=',
			'reg':r'\b(\w{2}\d{9}GB)\b'
		},
	]


	#TEST EACH POSSIBLE COMBINATION
        for entry in tracking_urls:
            if re.search(entry['reg'], tracking_number, flags=re.IGNORECASE):
                return entry['url'] + tracking_number.upper()

	# TRIM LEADING ZEROES AND TRY AGAIN
	# https://github.com/darkain/php-tracking-urls/issues/4
        if tracking_number.startswith("0"):
                return get_tracking_url(tracking_number.lstrip("0"))

	#NO MATCH FOUND, RETURN FALSE
        return False


def get_service_name(trackid):
        service = urllib.parse.urlparse(get_tracking_url(trackid)).hostname
        service_parts = service.split(".")
        return service_parts[-2].upper()
