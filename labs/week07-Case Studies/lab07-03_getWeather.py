import requests
import json
from xlwt import *

url = "https://prodapi.metweb.ie/observations/newport-furnace/today"
response = requests.get(url)
data = response.json()

# save to JSON file
filename = 'weatherReport.json'

# # write JSON data
f = open(filename, 'w')
json.dump(data, f, indent=4)

# write to excel file
w = Workbook()
ws = w.add_sheet('rptData')

# header row
rowNumber = 0
ws.write(rowNumber, 0, "name")
ws.write(rowNumber, 1, "temperature")
ws.write(rowNumber, 2, "symbol")
ws.write(rowNumber, 3, "weatherDescription")
ws.write(rowNumber, 4, "text")
ws.write(rowNumber, 5, "windSpeed")
ws.write(rowNumber, 6, "windGust")
ws.write(rowNumber, 7, "cardinalWindDirection")
ws.write(rowNumber, 8, "windDirection")
ws.write(rowNumber, 9, "humidity")
ws.write(rowNumber, 10, "rainfall")
ws.write(rowNumber, 11, "pressure")
ws.write(rowNumber, 12, "dayName")
ws.write(rowNumber, 13, "date")
ws.write(rowNumber, 14, "reportTime")
rowNumber += 1

for row in data:
    if ("name" in row):
        ws.write(rowNumber, 0, row["name"])
    if ("temperature" in row):
        ws.write(rowNumber, 1, row["temperature"])
    if ("symbol" in row):
        ws.write(rowNumber, 2, row["symbol"])
    if ("weatherDescription" in row):
        ws.write(rowNumber, 3, row["weatherDescription"])
    if ("text" in row):
        ws.write(rowNumber, 4, row["text"])
    if ("windSpeed" in row):
        ws.write(rowNumber, 5, row["windSpeed"])
    if ("windGust" in row):
        ws.write(rowNumber, 6, row["windGust"])
    if ("cardinalWindDirection" in row):
        ws.write(rowNumber, 7, row["cardinalWindDirection"])
    if ("windDirection" in row):
        ws.write(rowNumber, 8, row["windDirection"])
    if ("humidity" in row):
        ws.write(rowNumber, 9, row["humidity"])
    if ("rainfall" in row):
        ws.write(rowNumber, 10, row["rainfall"])
    if ("pressure" in row):
        ws.write(rowNumber, 11, row["pressure"])
    if ("dayName" in row):
        ws.write(rowNumber, 12, row["dayName"])
    if ("date" in row):
        ws.write(rowNumber, 13, row["date"])
    if ("reportTime" in row):
        ws.write(rowNumber, 14, row["reportTime"])
    rowNumber += 1









#    # print(rptName)
#     url = "https://reports.sem-o.com/api/v1/documents/" + rptName
#     # print(url)
#     response = requests.get(url)
#     aReport = response.json()
#     # subsequent rows
#     for row in aReport["rows"]:
#         # print(row["ImbalancePrice"])
#         ws.write(rowNumber, 0, row["StartTime"])
#         ws.write(rowNumber, 1, row["EndTime"])
#         if ("ImbalanceVolume" in row):
#             ws.write(rowNumber, 2, row["ImbalanceVolume"])
#         if ("ImbalancePrice" in row):
#             ws.write(rowNumber, 3, row["ImbalancePrice"])
#         if ("ImbalanceCost" in row):
#             ws.write(rowNumber, 4, row["ImbalanceCost"])
#         rowNumber += 1
w.save("weatherReport.xls")