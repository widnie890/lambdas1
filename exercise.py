
import csv
from functools import reduce

#PART 1
#read in data from DP and translating into dictionaries
reader = csv.DictReader(open("911_Calls_For_Service_(Last_30_Days).csv"))
reader = list(reader)
type(reader)
#using filter with lambda functions to exclude
#empty zip codes and neighborhoods
exclusions = list(filter(lambda row: row["zip_code"] != "" and row["zip_code"] != "0" and row["zip_code"] != "Null" and
row["neighborhood"] != "" and row["neighborhood"] != "Null" and row["neighborhood"] != "0",reader))

#using lambda functions and reduce to calculate averages
rtlist = list(filter(lambda row: row["totalresponsetime"] != "",reader ))
responsetime = reduce(lambda rt1, reader: rt1 + float(reader["totalresponsetime"]),rtlist, 0)
avgresponsetime = responsetime/len(rtlist)
print(f"The average response time is {avgresponsetime}")

dtlist = list(filter(lambda row: row["dispatchtime"] != "", reader))
dispatchtime = reduce(lambda dt1, reader: dt1 + float(reader["dispatchtime"]), dtlist, 0)
avgdispatchtime = dispatchtime/len(dtlist)
print(f"The average dispatch time is {avgdispatchtime}")

ttlist = list(filter(lambda row: row["totaltime"] != "",reader))
type(ttlist)
totaltime = reduce(lambda tt1, reader: tt1 + float(reader["totaltime"]), ttlist,0)
avgtotaltime = totaltime/len(ttlist)
print(f"The average total time is {avgtotaltime}")



#PART 2
