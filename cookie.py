__author__ = 'hzsunyuda'
import cookielib, urllib2
import sys
reload(sys)

argv = sys.argv
sys.setdefaultencoding("gbk")

cookie = cookielib.MozillaCookieJar()
cookie.load('localCookies.txt', ignore_discard=True, ignore_expires=True)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
scores = {}
words = []
def init():
    global scores
    global words
    f = open('out.html','w')
    f.close()

    t = open("word.txt","r")
    word = t.readline()
    while word:
        word = word.strip()
        if word == "":
            word = t.readline()
            continue
        temp = word.split(":")
        scores[temp[0]] = int(temp[1])
        words.append(temp[0])
        word = t.readline()
    t.close()

    req = urllib2.Request("http://ty.netease.com/forum.php?mod=guide&view=newthread")
    response = opener.open(req)
    body = response.read()
    num = body.find("normalthread_")
    maxnum = body[num+len("normalthread_"):num+len("normalthread_")+6]
    if argv.__len__() > 1:
        search(int(maxnum),int(argv[1]))
    else:
        search(int(maxnum))

def check(str):
    total = 0
    for word in words:
        if word in str:
            total = total + str.count(word)*scores[word]
    return total




def search(maxnum,num = 500):
    start = 1
    for a in range(maxnum-num,maxnum):
        f = open("out.html","a")
        url = "http://ty.netease.com/thread-%d-1-1.html"%a
        print "Now:%d,url = %s"%(start,url)
        start = start + 1
        req = urllib2.Request(url)
        response = opener.open(req)
        body = response.read()

        first = body.find("authorposton")
        end = body.find("</em>",first)
        timebody = body[first:end]

        first = body.find("<title>")+len("<title>")
        end = body.find("</title>")
        title = body[first:end]
        title = title.split("_")[0]

        time = ""
        if "<span" in timebody:
            s = timebody.find('title="') + len('title="')
            time = u"发表于 " + timebody[s:s+18]
        else:
            s = timebody.find('">')
            time = timebody[s:end]

        score = check(body)
        if score > 0 :
            space = ""
            if score < 10:
                space="   &nbsp;&nbsp;&nbsp;"
            elif score < 100:
                space="  &nbsp;&nbsp;"
            elif score < 1000:
                space=" &nbsp;"
            f.write('score:'+str(score)+space+'<a href="'+url+'">'+title+'</a>'+time+'<br>'+'\n')
        f.close()


init()
