#-*-coding:utf-8-*-

class HtmlOutputer(object):
    def __init__(self): #建立列表存放的数据
        self.datas = []

    def collect_data(self,data): #收集数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):  #将收集好的数据写出到一个html文件中
        fout = open('output.html','w') #建立文件输出对象

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>") #输出成表格形式

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url']) #输出data的url
            fout.write("<td>%s</td>"%data['title'].encode('utf-8')) #输出data的title
            fout.write("<td>%s</td>"%data['summary'].encode('utf-8')) #输出data的summary
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("<body>")
        fout.write("<table>")

        fout.close()
