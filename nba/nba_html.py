from urllib import request
from urllib.parse import quote
import string
class nbaHtml :
    def __init__(self):
        pass
    def getContent(self,url):
        if(url is None) :
            return None
        url_ = quote(url,safe=string.printable)
        response = request.urlopen(url_)
      #  print(response.read().decode("utf8"))
        return response.read().decode("utf8")
