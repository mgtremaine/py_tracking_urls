# Python3 Package Tracking URL Library

## About
Python Package Tracking URL Library is used to convert package tracking numbers
into their respective shipper's online tracking URL format. Based on the Original php code
by Darkain Multimedia Copyright (c) 2012, 2017

Supported shippers:
* United States Postal Service (USPS)
* United Parcel Service (UPS)
* Federal Express (FedEx)
* OnTrac
* DHL
* RoyalMail

## License
This software library is licensed under the BSD 2-clause license, and may be
freely used in any project which is compatible with this license.

## Example
Usage:
```python3
tracking = '1Z9999W99999999999';
url = get_tracking_url($tracking);
print(url)
```

Output:
```
http://wwwapps.ups.com/WebTracking/processInputRequest?TypeOfInquiryNumber=T&InquiryNumber1=1Z9999W99999999999
```

