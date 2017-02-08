#-*-coding:utf-8-*-

import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object): #创建SpiderMain方法
    def __init__(self):
        self.urls = url_manager.UrlManager() #初始化启动管理器
        self.downloader = html_downloader.HtmlDownloader() #初始化启动下载器
        self.parser = html_parser.HtmlParser() #初始化启动解析器
        self.outputer = html_outputer.HtmlOutputer() #启动初始化输出器

    def craw(self,root_url):
        count = 1 #记录当前爬取的是第几个url
        self.urls.add_new_url(root_url) #把入口url添加进url管理器中
        while self.urls.has_new_url(): #如果有待爬取的url
            try:
                new_url = self.urls.get_new_url() #取一个url出来
                print 'craw %d:%s' % (count,new_url) #打印出取的url是第几个url
                html_cont = self.downloader.download(new_url) #下载对应的界面
                new_urls,new_data = self.parser.parse(new_url,html_cont) #下载好后，进行页面的解析，得到新的url和数据
                self.urls.add_new_urls(new_urls) #把新的url补充进url管理器中
                self.outputer.collect_data(new_data) #进行数据的收集

                if count == 100: #目标是爬取100个页面
                    break
                count = count + 1
            except Exception,e:
                print e
                print 'craw failed'
        self.outputer.output_html()  #输出output收集下载好的数据
        print 'ok'



if __name__ == "__main__": #编写main函数
    root_url = "http://baike.baidu.com/view/21087.html" #设置入口的url
    obj_spider = SpiderMain()  #创建obj_spider
    obj_spider.craw(root_url)  #调用pider的craw方法启动爬虫
