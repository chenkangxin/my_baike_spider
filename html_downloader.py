#-*-coding:utf-8-*-
import urllib2
class HtmlDownloader(object):


    def download(self,url):
        if url is None:
            return None

        response = urllib2.urlopen(url)  #请求url的内容

        if response.getcode()!= 200:
            return None

        return response.read()  #返回下载好的内容

