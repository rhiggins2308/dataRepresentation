from bs4 import BeautifulSoup
with open("../week02-Javascript/carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')
# print (soup.tr)
rows = soup.findAll("tr")
for row in rows:
    # print("------")
    # print(row)
    cols = row.findAll("td")
    dataList = []
    for col in cols:
        # print(col.text)
        dataList.append(col.text)
    print(dataList)