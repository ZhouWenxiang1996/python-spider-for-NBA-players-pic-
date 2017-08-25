from nba_html import  nbaHtml
from nba_url import  nbaUrl
from nba_parse import HtmlParse

class nbaMain :

    def __init__(self):
        self.urlmanage = nbaUrl()
        self.html = nbaHtml()
        self.myParse = HtmlParse()
    def do(self, url):
        content = self.html.getContent(url)
        iurl = "http://stat-nba.com/playerList.php"
        news = self.myParse.parse(iurl,content) #所有球员的详细资料的地址
        # print("修改过的地址："+news)
        #new = news[0]
        #name, find1, findpic = self.myParse.getPlayer(new) #分别为球员详细资料的content 与 球员相片的地址
        #self.myParse.getPic(findpic)
        mylist= self.myParse.getAllPlayers(news)
        #self.myParse.getPics(mylist)
        #self.myParse.test()

if __name__ == "__main__" :

    url = "http://stat-nba.com/playerList.php"
    nba = nbaMain()
    nba.do(url)


