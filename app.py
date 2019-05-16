#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests , json , sys

api = 'http://api.ipstack.com/'

token = '7eefd3e65422bec69d7c8aef5a80c03e'

header = {
	'cache-control' : 'public, max-age=14400',
	'cf-cache-status' : 'MISS',
	'cf-ray' : '4d6b585a4f32ce27-LHR',
	'content-encoding' : 'br',
	'content-type' : 'application/json; Charset=UTF-8',
	'server' : 'cloudflare',
	'status' : '200',
	'strict-transport-security' : 'max-age=0; includeSubDomains',
	'vary' : 'Accept-Encoding',
	'x-request-time' : '0.157'
}

def main():
	try:
		url = str(input("IP : "))
		if ( url == "" ):
			print("[!] Gagal mendapatkan data ...")
			pass
		else:
			r = requests.get(api + url + '?access_key=' + token , headers=header)
			y = json.loads(r.text)
			print("-"*25)
			print("IP : " + y["ip"])
			print("Type : " + y["type"])
			print("Continent Code : " + y["continent_code"])
			print("Continent Name : " + y["continent_name"])
			print("Country Code : " + y["country_code"])
			print("Country Name : " + y["country_name"])
			print("Region Code : " + y["region_code"])
			print("Region Name : " + y["region_name"])
			print("City : " + y["city"])
			print("Zip Code : " + y["zip"])
			print("Location : https://www.latlong.net/c/?lat="+str(y["latitude"])+str("&")+str("long=")+str(y["longitude"]))
		pass
	except KeyboardInterrupt:
		print("[!] Gagal mendapatkan data ...")
		sys.exit()

if __name__ == '__main__':
	main()