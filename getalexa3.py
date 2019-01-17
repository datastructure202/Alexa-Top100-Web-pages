import os
import sys

main_list = [

"https://www.so.com",
"https://www.soundcloud.com",
"https://www.quora.com",
"https://www.aws.amazon.com",
"https://www.ask.com",
"https://www.nytimes.com",
"https://www.naver.com",
"https://www.ettoday.net",
"https://www.adf.ly",
"https://www.dailymotion.com",
"https://www.onlinesbi.com",
"https://www.steamcommunity.com",
"https://www.salesforce.com",
"https://www.espn.com",
"https://www.stackexchange.com",
"https://www.blogger.com",
"https://www.chase.com",
"https://www.vimeo.com",
"https://www.vice.com",
"https://www.theguardian.com",
"https://www.blastingnews.com",
"https://www.tribunnews.com",
"https://www.steampowered.com",
"https://www.avito.ru",
"https://www.globo.com",
"https://www.openload.co",
"https://www.spotify.com"

]

def main():
	for site in main_list:
		os.system("sudo wget -E -H -k -K -p --no-check-certificate " + site)

main()