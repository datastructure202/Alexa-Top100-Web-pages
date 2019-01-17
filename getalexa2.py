import os
import sys

main_list = [

"https://www.imdb.com",
"https://www.github.com",
"https://www.blogspot.com",
"https://www.pinterest.com",
"https://www.csdn.net",
"https://www.wikia.com",
"https://www.apple.com",
"https://www.popads.net",
"https://www.office.com",
"https://www.paypal.com",
"https://www.microsoftonline.com",
"https://www.diply.com",
"https://www.adobe.com",
"https://www.coccoc.com",
"https://www.craigslist.org",
"https://www.nicovideo.jp",
"https://www.dropbox.com",
"https://www.booking.com",
"https://www.thepiratebay.org",
"https://www.bbc.co.uk",
"https://www.savefrom.net",
"https://www.mozilla.org",
"https://www.rakuten.co.jp",
"https://www.uptodown.com"


]

def main():
	for site in main_list:
		os.system("sudo wget -E -H -k -K -p --no-check-certificate " + site)

main()
