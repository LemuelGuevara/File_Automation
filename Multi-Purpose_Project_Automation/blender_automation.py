import os
import subprocess
import sys

root = "/mnt/d/Blender Projects"
file_tree = ["Materials", "Models","Renders", "References"]
blender_path = "/mnt/c/Program Files/Blender Foundation/Blender 2.83/blender.exe"

class Blender_Automation:
    def __init__(self, project_name):
        self.project_name = project_name
        self.file_tree = file_tree
        self.blender_path = blender_path
        self.root_path = root

    def createProject(self):
        self.project_path = os.path.join(self.root_path, self.project_name)
        os.mkdir(self.project_path)
        os.chdir(self.project_path)
        
        self.blender_file = open(self.project_name + '.blend', "w+")
        
        try:
            for folder in self.file_tree:
                os.mkdir(os.path.join(self.project_path, folder))
        
        except Exception:
            print("Project already exists.")
        