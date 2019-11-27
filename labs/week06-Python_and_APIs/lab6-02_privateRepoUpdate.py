import requests
import json

url = "https://api.github.com/repos/rhiggins2308/datarep_private/testfile.txt"

# remove - before last digit of apiKey before running
apiKey = 'c0ce726250fb27b921909c4bde125ef08afa88c-8'
filename = "myRepoUpdate.json"

dataString = {"testfile.txt": "hello"}

response = requests.put(url, json=dataString, auth=('token',apiKey))
# response = requests.get(url, auth=('token',apiKey))
# print (response.json())

repoJSON = response.json()

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)