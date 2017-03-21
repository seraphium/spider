import urllib
import urllib2

class BDTB:
    def __init__(self, baseURL, seeLZ):
        self.baseURL = baseURL
        self.seeLZ =  '?see_lz=' + str(seeLZ)

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + "&pn=" + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
               print u"loading baidu tieba failed", e.reason
               return None


baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
bdtb.getPage(1)

