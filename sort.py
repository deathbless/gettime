# __author__ = 'hzsunyuda'
# a = open("out.txt","r")
# num = 1
# fifty = 0
# hundred = 0
# line = a.readline()
# out = []
# while line:
#     num = num + 1
#     score = int(line[6:10])
#     if score >= 50:
#         fifty = fifty + 1
#     if score >= 100:
#         hundred = hundred + 1
#     out.append((line,score))
#     line = a.readline()
#
# a.close()
# f = open("sort.txt","w")
# f.write("Total:%d Important(>=50):%d Very Important(>=100):%d\n<br>"%(num,fifty,hundred))
# out.sort(lambda x,y:cmp(y[1],x[1]))
# for x in out:
#     f.write(x[0]+'\n')
# f.close()
import sys
argv = sys.argv
print argv[0],argv[1],argv.__len__()