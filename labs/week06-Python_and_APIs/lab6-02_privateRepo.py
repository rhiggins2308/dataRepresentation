import requests
import json

url = "https://api.github.com/repos/datarepresentationstudent/aPrivateOne"

# remove - before last digit of apiKey before running
apiKey = '757b586c0231f8eb540436c1c7c9f678843a653-7'
filename = "privateRepoDump.json"

response = requests.get(url, auth=('token',apiKey))
# print (response.json())

repoJSON = response.json()

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)