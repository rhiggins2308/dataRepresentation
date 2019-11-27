# Just did this lab with my own repo ... got sick of the token situation, sorry
from github import Github
import requests

# remove the minus sign from the key
g = Github("c0ce726250fb27b921909c4bde125ef08afa88c-8")

# for repo in g.get_user().get_repos():
#     print(repo.name)

repo = g.get_repo("rhiggins2308/datarep_private")
# print(repo.clone_url)

fileInfo = repo.get_contents("testfile.txt")
urlOfFile = fileInfo.download_url
# print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
# print (contentOfFile)

# newContents = contentOfFile + " I love lamp! \n"
newContents = contentOfFile + " LOUD NOISES! \n"
# print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)