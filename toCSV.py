import csv
import json
<<<<<<< HEAD
with open('file.csv', 'rb') as f:
     reader = csv.reader(f)
     your_list=list(reader)

print your_list
=======
import time
with open('TTC.UK.ALLBOLUS_READINGS_LOG.csv', "rb") as f:
     reader = csv.reader(f)
     totalCSVBolus=list(reader)
with open('TTC.UK.ALLCGM_READINGS_LOG.csv', "rb") as f:
     reader = csv.reader(f)
     totalCSVCGM=list(reader)
totalCSVFieldsDate=13775
bolusLength=971
totalCSVFood=59


with open("TTC.UK.ALLFOOD_LOG.csv", "rb") as g:
    reader = csv.reader(g)
    totalFoodCSV=list(reader)

for i in xrange(0,totalCSVFood):
     currentDate= totalFoodCSV[i][26]
     for j in xrange(0, totalCSVFieldsDate):
         if (currentDate[0:14]==totalCSVCGM[j][24][0:14]):
             totalFoodCSV[i].append(totalCSVCGM[j][18])
             break
     for j in xrange(0, bolusLength):
         if (currentDate[0:12]==totalCSVBolus[j][28][0:12]):
            totalFoodCSV[i].append(totalCSVBolus[j][18])
            break

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(totalFoodCSV)
>>>>>>> f6b3320a9b2973ff7dd08fd0028c25b0effef889







#def cleanTimes():

#    str neareastString

#    for eachCategory in x:
#        for eachReading in eachCategory:
#            if ("readingDate" in eachReading):
#                nearestString=eachCategory["readingDate"][11:13]
#                eachCategory["readingDate"][11]=str((int(nearestString)/6)*6)[0]
#                eachCategory["readingDate"][12]=str((int(nearestString/6)*6)[1]
#           else:
#                eachCategory["readingDate"]





#def fetchMatches(eachReading["readingDate")

#   returning=[]


#d={}
#for eachReading in x["bloodGlucose"]:
#     if ("readingDate" in eachReading):
#         d[eachReading["readingDate"]]=fetchMatches(eachCategory, eachReading["readingDate"])




