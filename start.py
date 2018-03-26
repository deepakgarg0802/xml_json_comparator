# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
#
# html = urlopen("http://www.google.com/")
# soup= BeautifulSoup(html)
# print(soup.prettify())

from bs4 import BeautifulSoup
import urllib

post_params = {
    param1 : val1,
    param2 : val2,
    param3 : val3
        }
post_args = urllib.urlencode(post_params)

url = 'http://www.website.com/'
fp = urllib.urlopen(url, post_args)
soup = BeautifulSoup(fp)