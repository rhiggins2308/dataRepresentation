import requests
import json
from xlwt import *

dateToSearch = "2019-12-05"
# url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>"+dateToSearch
response = requests.get(url)
data = response.json()

totalPages = data["pagination"]["totalPages"]
rptList = []

pageNo = 1
while pageNo <= totalPages:
    pageUrl = url + "&page" + str(pageNo)
    data = requests.get(pageUrl).json()
    
    for item in data["items"]:
        # print(item["ResourceName"])
        rptList.append(item["ResourceName"])
    pageNo += 1

# write to excel file
w = Workbook()
ws = w.add_sheet('rptData')

# header row
rowNumber = 0
ws.write(rowNumber, 0, "StartTime")
ws.write(rowNumber, 1, "EndTime")
ws.write(rowNumber, 2, "ImbalanceVolume")
ws.write(rowNumber, 3, "ImbalancePrice")
ws.write(rowNumber, 4, "ImbalanceCost")
rowNumber += 1


for rptName in rptList:
    # print(rptName)
    url = "https://reports.sem-o.com/api/v1/documents/" + rptName
    # print(url)
    response = requests.get(url)
    aReport = response.json()
    # subsequent rows
    for row in aReport["rows"]:
        # print(row["ImbalancePrice"])
        ws.write(rowNumber, 0, row["StartTime"])
        ws.write(rowNumber, 1, row["EndTime"])
        if ("ImbalanceVolume" in row):
            ws.write(rowNumber, 2, row["ImbalanceVolume"])
        if ("ImbalancePrice" in row):
            ws.write(rowNumber, 3, row["ImbalancePrice"])
        if ("ImbalanceCost" in row):
            ws.write(rowNumber, 4, row["ImbalanceCost"])
        rowNumber += 1
w.save("balance.xls")


# # save to JSON file
# filename = 'allreports.json'

# # write JSON data
# f = open(filename, 'w')
# json.dump(data, f, indent=4)