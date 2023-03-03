import datetime

a = datetime.datetime.now()
b = a-datetime.timedelta(1)
print((a-b).days*3600*24,"seconds difference") 