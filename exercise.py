
import csv
from functools import reduce

#PART 1
#read in data from DP and translating into dictionaries
reader = csv.DictReader(open("911_Calls_For_Service.csv"))

#using filter with lambda functions to exclude
#empty zip codes and neighborhoods
exclusions = list(filter(lambda row: row["zip_code"] != "" and row["neighborhood"] != "" 
and row["totalresponsetime"] != "" and row["dispatchtime"] != "" and row["totaltime"] != "" ))

#using lambda functions and reduce to calculate averages
responsetime = reduce(lambda rt1, "totalresponsetime": rt1 + reader["totalresponsetime"] * (reader["totalresponsetime"] - 1), reader, 0)

dispatchtime = reduce(lambda dt1, dict)
 