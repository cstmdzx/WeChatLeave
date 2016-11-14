# -*- coding: utf-8 -*-
reload(sys)  # 用来使后面的输出是中文
sys.setdefaultencoding('utf-8')
fileName = open('WeChatIdToName.txt', 'r')
linesName = fileName.readlines()
db = MySQLdb.connect('localhost', 'root', 'dbis23508468', 'WeChatLeave')
cursor = db.cursor()
for eachName in linesName:
    eachName = eachName.replace('\n', '')
    eachName = eachName.replace('\r', '')
    words = eachName.split(' ')

    cursor.execute('insert into WeChatIdToName values(\'' + words[0].__str__() + '\', \'' + words[1].__str__() + '\')')
db.commit()
db.close()

