#!/usr/bin/python3
import os
import sys

gitCommands = [
    "git init",
    "touch README.md",
    "git add .",
    ("git commit -m Initial_Commit"),
    "hub create",
    "git push -u origin master",
    "code ."
]

root = "/mnt/c/Users/Lemue/Desktop/Python_Projects"

class Python_Project_Automation:
    def __init__(self, projectName):
        self.projectName = projectName
        self.gitInit = gitCommands
        self.rootPath = root
        
    def createProject(self):
        self.projectName = os.path.join(self.rootPath, self.projectName)

        try:
            os.mkdir(self.projectName)

            return self.initProject()

        except Exception:
            print("Project already exists.")
            sys.exit()

    def initProject(self):
        os.chdir(self.projectName)

        for command in self.gitInit:
            os.system(command)
