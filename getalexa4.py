import os
import sys

main_list = [

"https://www.flipkart.com",
"https://www.ladbible.com",
"https://www.deviantart.com",
"https://roblox.com",
"https://github.io",
"https://walmart.com",
"https://douyu.com",
"https://slideshare.net",
"http://www.w3schools.com",
"http://www.washingtonpost.com",
"http://www.etsy.com",
"http://www.rambler.ru",
"http://www.alibaba.com",
"http://www.sogou.com",
"http://www.nih.gov",
"http://www.softonic.com",
"http://www.babytree.com",
"http://www.9gag.com",
"http://www.slack.com",
"http://www.bankofamerica.com",
"http://www.mercadolivre.com.br",
"http://www.4chan.org"

]

def main():
	for site in main_list:
		os.system("sudo wget -E -H -k -K -p --no-check-certificate " + site)

main()