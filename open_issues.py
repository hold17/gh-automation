import json, sys
import getpass
import requests

topUrl = "https://api.github.com"
userUrl = "%s/orgs/hold17/issues" % topUrl
repoUrl = "%s/repos/hold17/cphindustries" % topUrl

username = input("Username: ")
password = getpass.getpass("Password: ")

issuesReq = requests.get("%s/issues?state=open" % repoUrl, auth=(username, password))
issues = issuesReq.json()

print("Open issues: ")

notAssigned = 0
for issue in issues:
    assignee = issue["assignee"]
    if assignee == None:
        notAssigned = notAssigned + 1
        print(" - %s" % issue["title"])
    else:
        print(" - %s (%s)" % (issue["title"], assignee["login"]))

print("======================")
print("There are %s open issues" % len(issues))
print("%s issues has been assigned." % notAssigned)
