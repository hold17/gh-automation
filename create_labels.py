import json, sys
import getpass
import requests

topUrl = "https://api.github.com"
orgName = "hold17"

def CreateLabels(username, password, repoName):
    url = "%s/repos/%s/%s/labels" % (topUrl, orgName, repoName)
    print("Posting labels...")

    jsonObjs = [
        {"name": "breaking", "color": "fbca04"},
        {"name": "needs testing", "color": "39efbc"},
        {"name": "new-feature", "color": "250920"}
    ]

    for jsonObj in jsonObjs:
        testR = requests.post("%s" % url, auth=(username, password), json=jsonObj)

    print("All labels posted")

def GetAllLabels(username, password, repoName):
    url = "%s/repos/%s/%s/labels" % (topUrl, orgName, repoName)
    labelsReq = requests.get("%s" % url, auth=(username, password))
    labels = labelsReq.json()

    #print(labelsReq.url)
    print("Current labels: ")
    #print(labels)
    for label in labels:
        print(" - %s" % label["name"])

def GetRepos(username, password):
    url = "%s/users/%s/repos" % (topUrl, orgName)
    print("\nGetting repos...")
    r = requests.get(url, auth=(username, password))
    allRepos = r.json()
    i = 0
    for rep in allRepos:
        print(" - [%s] %s" % (i, rep["name"]))
        i = i + 1
    return allRepos

repoUrl = "%s/repos/hold17/cphindustries" % topUrl

username = input("Username: ")
password = getpass.getpass("Password: ")


allRepos = GetRepos(username, password)
repo = None

if len(allRepos) > 1:
    repoIndex = input("Select repo: ")
    repo = allRepos[int(repoIndex)]
    print("Selected %s." % repo["name"])
elif len(allRepos) == 1:
    repo = allRepos[0]
    print("Only 1 repository. Selected repository is %s." % repo["name"])
else:
    print("No repositories.")
    sys.exit(1)

#CreateLabels(username, password, repo["name"])
repoName = repo["name"]
GetAllLabels(username, password, repoName)
#print("Repository: %s" % repo)


#GetAllLabels(username, password)






