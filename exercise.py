
import csv
from functools import reduce

#PART 1
#read in data from DP and translating into dictionaries
reader = csv.DictReader(open("911_Calls_For_Service.csv"))

#using filter with lambda functions to exclude
#empty zip codes and neighborhoods
exclusions = list(filter(lambda row: row["zip_code"] != "" and row["zip_code"] != "0" and row["zip_code"] != "Null" and
row["neighborhood"] != "" and row["neighborhood"] != "Null" and row["neighborhood"] != "0" and 
row["totalresponsetime"] != "" and row["totalresponsetime"] != "0" and row["totalresponsetime"] != "None" and
row["dispatchtime"] != "" and row["dispatchtime"] != "0" and row["dispatchtime"] != "Null" and 
row["totaltime"] != "" and row["totaltime"] != "0" and row["totaltime"] != "Null",reader))

#using lambda functions and reduce to calculate averages
responsetime = reduce(lambda rt1, reader: rt1 + float(reader["totalresponsetime"]), reader, 0)
avgresponsetime = responsetime/len(exclusions)
print(f"The average response time is {avgresponsetime}")

dispatchtime = reduce(lambda dt1, reader: dt1 + float(reader["dispatchtime"]) * (reader["dispatchtime"] - 1), reader, 0)
avgdispatchtime = dispatchtime/len(exclusions)
print(f"The average dispatch time is {avgdispatchtime}")

totaltime = reduce(lambda tt1, reader: tt1 + float(reader["totaltime"]) * (reader["totaltime"] - 1), reader,0)
avgtotaltime = str(totaltime/len(exclusions))
print(f"The average total time is {avgtotaltime}")
 

#PART 2
