class nbaUrl :
    def __init__(self):
        self.old_url = set() # 已爬取的url
        self.new_url = set() # 待爬取的url
    def addToNew(self,url):
        if(url is None):
            return
        if(url  in self.new_url and url not in self.old_url) :
            self.old_url.add(url)
            self.new_url.remove(url)
    def addToNews(self, urls):
        if (urls is None or len(urls) == 0):
            return
        for url in urls:
            self.addToNew(url)
