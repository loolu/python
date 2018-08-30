#计算指定日期计算后N天是哪一天的方法
import datetime
def getday(y=2018,m=1,d=1,n=0):
    the_date = datetime.datetime(y,m,d)
    result_date = the_date + datetime.timedelta(days=n)
    d = result_date.strftime('%Y-%m-%d')
    return d

print(getday(2018,9,30,-9))
