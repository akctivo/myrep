import datetime
import time
import pytz


#t = time.time()

now1 = time.asctime()
print("Time now is: ", now1, "Pacific")
print("1 for east coast time, 2 for central time, 3 for mountain time, ")

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
#print("Time now is:", dt_utcnow)

t = int(input())

if t == 1:
    dt_east = dt_utcnow.astimezone(pytz.timezone("US/Eastern"))
    print("East coast time is: ", dt_east.time())


elif t == 2:
    dt_central = dt_utcnow.astimezone(pytz.timezone("US/Central"))
    print("Central time is: ", dt_central.time())


elif t == 3:
    dt_mountain = dt_utcnow.astimezone(pytz.timezone("US/Mountain"))
    print("Mountain time is:", dt_mountain.time())

else:
    print("Choice entered is not one of the available options")

