import urllib2, random

user_agents = [
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (X11; Linux i686; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
    'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.45 Safari/534.13',
    'Opera/9.80 (X11; Linux i686; U; en) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US))',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
]

connection_timeout = 90
random.seed()
user_agent = random.choice(user_agents)

#this is an instance of an opener, you have to use it, you know?
opener = urllib2.build_opener()
#the randomly chosen User-Agent gets added to this opener
opener.addheaders = [('User-Agent', user_agent)]

#this function is downloading the HTML, or reporting a failure
def get_url(url, referer_url=None):
    '''Downloads specified URL and returns its contents. Returns false
    on fail.'''
    retries = 5
    while retries > 0:
        try:
            if referer_url:
                req = urllib2.Request(url, headers={'accept': '*/*'})
                req.add_header('Referer', referer_url)
                page = opener.open(req)
            else:
                page = opener.open(url, None, connection_timeout)
        except urllib2.URLError, e:
            if hasattr(e, 'code') and e.code == 503:
                return e.read()
            else:
                print('Download failed.')
                retries -= 1
                if retries > 0:
                    print('Retrying...')
        else:
            return page.read()
    print('Maximum number of retries reached.')
    return False

#printing the return of get_url()
print (get_url("http://www.dotabuff.com"))
