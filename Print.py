import datetime
def Time():
    time = datetime.datetime.now()
    print ("Today's date %s/%s/%s" % (time.day, time.month, time.year))
    print ("The time is now  %s:%s:%s" % (time.hour, time.minute, time.second))
