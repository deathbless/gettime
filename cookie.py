__author__ = 'hzsunyuda'
import cookielib, urllib2

cookie = cookielib.MozillaCookieJar()
cookie.load('localCookies.txt', ignore_discard=True, ignore_expires=True)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

def init():
    f = open('out.txt','w')
    f.close()
    req = urllib2.Request("http://ty.netease.com/forum.php?mod=guide&view=newthread")
    response = opener.open(req)
    body = response.read()
    num = body.find("normalthread_251061")
    maxnum = body[num+13:num+19]
    search(int(maxnum))

def search(maxnum):
    for a in range(maxnum-500,maxnum):
        url = "http://ty.netease.com/thread-%d-1-1.html"%a
        req = urllib2.Request(url)
        response = opener.open(req)
        body = response.read()
        first = body.find("authorposton")
        end = body.find("</em>",first)
        mainbody = body[first:end]
        time = ""
        if "<span" in mainbody:
            s = mainbody.find('title="') + len('title="')
            time = u"发表于 " + mainbody[s:s+18]
        else:
            s = mainbody.find('">')
            time = mainbody[s:end]
        print time

init()
