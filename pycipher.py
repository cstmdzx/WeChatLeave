# -*- coding: utf-8 -*-
import sys
import MySQLdb
import re
import types

from pysqlcipher import dbapi2 as sqlite
from unixtime import timestamp_datetime


reload(sys)  # 用来使后面的输出是中文
sys.setdefaultencoding('utf-8')
fileRes = open('res', 'w')

sqlCipherConn = sqlite.connect('/home/nklyp/MicroMsg/9af554334ac9959186616787a46529bc/EnMicroMsg.db')
# sqlCipherConn.set_character_set('utf8')
sqlCipherCursor = sqlCipherConn.cursor()
sqlCipherCursor.execute("PRAGMA key='keycode'")
sqlCipherCursor.execute("PRAGMA cipher_use_hmac = off")
sqlCipherCursor.execute('''select * from message where talker=\'3793351452@chatroom\'''')
res = sqlCipherCursor.fetchall()
# print res
db = MySQLdb.connect('localhost', 'root', 'dbis23508468', 'WeChatLeave')
mySQLcursor = db.cursor()
db.set_character_set('utf8')
mySQLcursor.execute('SET NAMES utf8')
mySQLcursor.execute('SET CHARACTER SET utf8')
mySQLcursor.execute('SET character_set_connection=utf8')


# 需要一个正则来搞，匹配不出来就直接pass，明儿再说吧
patternReason = re.compile(u'\u56e0([\u4e00-\u9fa5]+)\u8bf7\u5047([\u4e00-\u9fa5]+|[\d]+[\u4e00-\u9fa5]+|[0-9]+[a-zA-Z]+|[0-9]\.[0-9]([\u4e00-\u9fa5]+)|[0-9]\.[0-9]([a-zA-Z]+))')
# -----------------------------因-----------------------请假---------------后面就是同学们发明的各种的时间格式------------
# 那些用续假来请假的，也是没谁了

for eachLine in res:
    # print eachLine
    strContent = eachLine[8]
    # print type(strContent)
    if type(strContent) is not types.UnicodeType:
        continue
    # print strContent
    intTime = eachLine[6]  # 这个是带毫秒的，所以后面除1000
    if strContent.find('请假') == -1:
        continue
        # print strContent
    # else:
        # continue
    fileRes.write(strContent + '\n')
    strContent = strContent.replace('\n', '')
    strContent = strContent.replace('\r', '')
    words = strContent.split(':')
    # print timestamp_datetime(intTime / 1000)
    intTime = intTime / 1000
    # print repr(words[1])
    # print words
    if words.__len__() < 2:

        match = patternReason.search(words[0])
        if match:
            strReason = match.group(1)
            strDuration = match.group(2)
            # print('insert into WeChatLeave(WeChatId, CreateTime, Reason, Duration) values(\'' + 'diguo963065060' + '\', ' + intTime.__str__() + ', \'' + strReason.__str__() + '\',\'' +  strDuration.__str__() + '\')')
            mySQLcursor.execute('insert into WeChatLeave(WeChatId, CreateTime, Reason, Duration) values(\'' + 'diguo963065060' + '\', ' + intTime.__str__() + ', \'' + strReason.__str__() + '\', \'' +  strDuration.__str__() + '\')')


    else:
        try:
            mySQLcursor.execute('select * from WeChatIdToName where WeChatId = \'' + words[0].__str__() + '\'')
            test = mySQLcursor.fetchall()
            if test.__len__() == 1:
                match = patternReason.search(words[1])
                # print match.__len__()
                if match:
                    strReason = match.group(1)
                    strDuration = match.group(2)
                    mySQLcursor.execute('insert into WeChatLeave(WeChatId, CreateTime, Reason, Duration) values(\'' + words[0].__str__() + '\', ' + intTime.__str__() + ', \'' + strReason.__str__() + '\', \''+ strDuration.__str__() +'\')')
                else:
                    print 'match error'
                    print words[1]
        except:
            db.rollback()
# file.write(res)
# c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
# conn.commit()
db.commit()
db.close()

