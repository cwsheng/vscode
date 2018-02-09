# -*- coding: utf-8 -*-
import urllib2

def openurl(url):
    web = urllib2.urlopen(url)
    content = web.read()
    print content