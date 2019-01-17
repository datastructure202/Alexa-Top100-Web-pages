import os
import sys

main_list = [

"https://www.google.com",
"https://www.youtube.com",
"https://www.baidu.com",
"https://www.wikipedia.org",
"https://www.reddit.com",
"https://www.qq.com",
"https://www.amazon.com",
"https://www.taobao.com",
"https://www.twitter.com",
"https://www.tmall.com",
"https://www.live.com",
"https://www.vk.com",
"https://www.instagram.com",
"https://www.sohu.com",
"https://www.jd.com",
"https://www.weibo.com",
"https://www.360.cn",
"https://www.linkedin.com",
"https://www.yandex.ru",
"https://www.netflix.com",
"https://www.bing.com",
"https://www.msn.com",
"https://www.twitch.tv",
"https://www.tumblr.com",
"https://www.alipay.com",
"https://www.mail.ru",
"https://www.microsoft.com",
"https://www.ok.ru",
"https://www.aliexpress.com",
"https://www.stackoverflow.com"

]

def main():
	for site in main_list:
		os.system("sudo wget -E -H -k -K -p --no-check-certificate " + site)

main()