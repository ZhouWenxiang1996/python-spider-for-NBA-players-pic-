from bs4 import BeautifulSoup
import re
from urllib import parse
from nba_html import  nbaHtml
import os
import requests
from nba_player import PlayerMsg
import pymysql

class HtmlParse :



    def parse(self,url,content): #获取列表，其中的元素为包含名字与地址的字典

        news = list()

        if(url is None or content is None):
            print("None...")
            return
        soup = BeautifulSoup(content,"html.parser")
        # al = soup.findAll('a', class_="allstarplayer",href=re.compile(r'./player/.*'))
        al = soup.findAll('a', class_=re.compile(r'player$'), href=re.compile(r'./player/.*'))
        #all = dict()
        i = 0
        for each in al :
            all = dict()
            all["name"] = each.span.get_text()
            all["href"] = each["href"]
            news.append(all)
            i+=1
        print("一共"+str(len(news))+"人")
        for eachs in news :
            print(eachs["name"],each["href"])
        return  news

    def getAllPlayers(self, news): #返回球员的元组资料列表
        j = 0
        mylist= list()
        if (news is None or len(news) == 0):
            return
        for new in news:
            name, player, pic_url = self.getPlayer(new)
            tuple1 = (name, player, pic_url)
            mylist.append(tuple1)
        self.storeToDataBase(mylist)
        return mylist
    def getPlayer(self,new): #返回包含名字、球员对象、图片资料的元组
        if(new is None) :
            return None
        new_url = new["href"]
        name = new["name"]
        old_url = "http://stat-nba.com/playerList.php"
        new_full_url = parse.urljoin(old_url,new_url)
        content = nbaHtml().getContent(new_full_url)
        soup = BeautifulSoup(content, "html.parser")
        find1 = soup.find('div', class_="detail")
        findpic = soup.find('img', src=re.compile(r'jpg$')).get("src")
        new_findpic = parse.urljoin(old_url, findpic)

        # find2 = soup.find('div', class_="row")
        # a = find2.get_text().split(":")
        # print(a[0],"&&",a[1])

        find2 = soup.findAll('div', class_="row", limit=6)

        list1 = list()
        for ss in find2 :
            #print(ss.get_text())
            array = ss.get_text().split(":")
            list1.append(array[1])

        print("*-------------------------------*")

        player = self.creatPlayerClass(name,list1)
        return name, player, new_findpic

    def getPic(self,pic_url):
        if not os.path.exists('nbaImage'):
            os.mkdir('nbaImage')

        try:
            pic = requests.get(pic_url, timeout=3)
        except requests.exceptions.ConnectionError:
            print("当前图片无法下载")
        file_name = "nbaImage/" + str(0) + ".jpg"
        print(os.path, file_name, sep='/')
        # 将图片存入本地
        fp = open(file_name, 'wb')
        fp.write(pic.content)  # 写入图片
        fp.close()

    def getPics(self, list):
        if not os.path.exists('nbaImage'):
            os.mkdir('nbaImage')
        i = 0
        for each in list:
            pic_url = each[2]
            try:
                pic = requests.get(pic_url, timeout=3)
            except requests.exceptions.ConnectionError:
                print("当前图片无法下载")
                continue
            file_name = "nbaImage/" + str(i) + ".jpg"
            print(os.path, file_name, sep='/')
            # 将图片存入本地
            fp = open(file_name, 'wb')
            fp.write(pic.content)  # 写入图片
            fp.close()
            i+=1

    def creatPlayerClass(self,name,list1): #返回球员对象
        player = PlayerMsg(name[1:-1], list1)
        player.toString()
        return player

    def storeToDataBase(self,mylist): #将信息存入数据库
        db = pymysql.connect(host="127.0.0.1",
                             port=3306,
                             user="root",
                             password="123456",
                             db="python",
                             charset="utf8"
                             )

        print(db)

        i = 1
        for each in mylist:
            sql = "insert into nba_player values( %d" % i
            sql += ", '" + each[1].name.replace("'", "\\\'")+"' , '"+each[1].English_name.replace("'", "\\\'")+"' , '"+each[1].pos+"' , '"+each[1].height+"' , '"+each[1].weight+"' , '"+each[1].birth+"' , '"+each[1].city+"')"
            print(sql)
            cursor = db.cursor()
            row = cursor.execute(sql)
            print(row)
            db.commit()
            cursor.close()
            i+=1
        db.close()





