import csv
import pymongo

coll=pymongo.MongoClient().sihu.mp4

with open("XXX.csv","w",newline="") as datacsv:
    csvwriter = csv.writer(datacsv,delimiter=' ',dialect = ("excel"))

    for item in coll.find():
        csvwriter.writerow(item['mp4'])