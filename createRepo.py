import json, sys
import getpass
import requests
import webbrowser

topUrl = "https://api.github.com"

print("WARNING: Does not work for organisation yet...")

def GetOrganisations(username, password):
    url = "%s/user/orgs" % topUrl

    orgsRequest = requests.get(url, auth=(username, password))
    orgs = orgsRequest.json()

    return orgs

def ListOrganisations(username, password, orgs):
    i = 1
    print(" - [0] %s" % username)
    for org in orgs:
        print(" - [%s] %s" % (i, org["login"]))
        i += 1

def GetOrganisationName(username, password, orgs):
    ListOrganisations(username, password, orgs)

    usrInput = input("Selected organisation: ")
    if usrInput == "0": 
        return username
    else:
        org = orgs[int(usrInput)]
        return org["login"]

def CreateRepository(username, password, orgName):
    isOrganisation = True
    if orgName == username:
        isOrganisation = False

    if (isOrganisation): 
        url = "%s/orgs/orgName/repos" % topUrl
    else:
        url = "%s/user/repos" % topUrl

    name = input("Repository Name: ")
    desc = input("Description: "),
    
    jsonArr = [
            {
                "name": name,
                "description": desc,
                "private": False,
                "has_issues": True,
                "has_projects": False,
                "has_wiki": True
                }
            ]

    print("Posting to %s..." % url)
    postRequest = requests.post(url, auth=(username, password), json=jsonArr[0])
    
    if isOrganisation: # TODO: For debugging only! Remove when fixed...
        print(postRequest.json())
    postedUrl = postRequest.json()["html_url"]

    print("Posted repo: %s" % postedUrl)
    openInBrowser = input("Open in webbrowser [Y/n]?" ).lower()

    if openInBrowser == "n" or openInBrowser == "no" or openInBrowser == "nope":
        return
    webbrowser.open(postedUrl)

username = input("Username: ")
password = getpass.getpass("Password: ")

orgs = GetOrganisations(username, password)
orgName = GetOrganisationName(username, password, orgs)

CreateRepository(username, password, orgName)
