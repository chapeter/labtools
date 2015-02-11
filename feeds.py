#!/usr/bin/env python3
__author__ = 'chapeter@cisco.com'

import feedparser
import urllib
import urllib3
from html.parser import HTMLParser

#raw_html = feedparser.parse("https://tools.cisco.com/support/cwsx/notify/pub/feedservice/service/en_US/285954710/10014/30")

#print(r.data.decode('utf-8'))

#sock = urllib.request("https://tools.cisco.com/support/cwsx/notify/pub/feedservice/service/en_US/285954710/10014/30")

allrelease = []

class MyHTMLParser(HTMLParser):
    global allrelease
#    def handle_starttag(self, tag, attrs):
#        print("Encountered a start tag:", tag)
#    def handle_endtag(self, tag):
#        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        #print("Encountered some data  :", data)
        if "release" in data:
            allrelease.append(data.split("release=",1)[1])



def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

#print(allrelease)

def get_code():
    url = "https://tools.cisco.com/support/cwsx/notify/pub/feedservice/service/en_US/285954710/10014/30"
    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('GET',url)
    parser = MyHTMLParser()
    parser.feed(r.data.decode('utf-8'))

    code = (sorted(remove_duplicates(allrelease), reverse=True))
    #print(code[0])
    return code[0]

def get_code3000():
    url = "https://tools.cisco.com/support/cwsx/notify/pub/feedservice/service/en_US/283970187/10014/30"
    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('GET',url)
    parser = MyHTMLParser()
    parser.feed(r.data.decode('utf-8'))

    code = (sorted(remove_duplicates(allrelease), reverse=True))
    #print(code[0])
    return code[0]

#print(get_code3000())