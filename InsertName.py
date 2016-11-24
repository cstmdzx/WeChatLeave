# -*- coding: utf-8 -*-
import sys
import MySQLdb

reload(sys)  # 用来使后面的输出是中文
sys.setdefaultencoding('utf-8')
fileName = open('id2', 'r')
linesName = fileName.readlines()
db = MySQLdb.connect('localhost', 'root', 'dbis23508468', 'WeChatLeave')
cursor = db.cursor()

# to ensure that the characters are Chinese after insertion
db.set_character_set('utf8')
cursor.execute('SET NAMES utf8')
cursor.execute('SET CHARACTER SET utf8')
cursor.execute('SET character_set_connection=utf8')

for eachName in linesName:
    eachName = eachName.replace('^M', '')



    eachName = eachName.replace('\n', '')
    print eachName
    eachName = eachName.replace('\r', '')
    words = eachName.split(' ')

    print eachName
    print words[1]
    sql = 'update WeChatIdToName set StudentName = \'' + words[1].__str__() + '\' where WeChatId = \'' + words[0].__str__() + '\''
    sql2 = 'update WeChatIdToName set StudentName = \'yu用来使后\' where WeChatId = \'yu327018593\''
    cursor.execute(sql)
    print sql
    db.commit()
db.close()

