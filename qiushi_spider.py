#!/usr/bin/python
#encoding=utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
page=10
headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}
for i in range (page): 
  print ('这是第%s张页面内容！' % i)
  print 
  url='http://www.qiushibaike.com/hot/page/'+str(i)  
  try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content=response.read().decode('utf-8')
  except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason
  content1=BeautifulSoup(content)   
  content2=content1.select('div[class="content"]')
  for content3 in content2:
    #content4=content3.select('span')
    #print type(content4[0])类型是对象，所以不能直接decode，必须先string
    #print content4[0].string
    print content3.span.string
    print
