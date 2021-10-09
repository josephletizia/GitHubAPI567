# Author: Joseph Letizia
# SSW 567
# Homework 4a

import json
import requests


def repo_count(u):

    output = {}

    if(type(u) != str):
        return "Not a valid input for the user"

    else:
        url = "https://api.github.com/users/"+u+"/repos"
        data = requests.get(url).json()

        for repo in data:
            commits = "https://api.github.com/repos/"+u+"/" + \
                repo['name']+"/commits?page=1&per_page=100"
            commitsData = requests.get(commits).json()
            commitCount = len(commitsData)

            print("Repo Name: "+repo['name'])
            print("Commits: "+str(commitCount))
            print()
            output[repo['name']] = len(commits)
        #print(len(commits))
    return output

repo_count('josephletizia')
