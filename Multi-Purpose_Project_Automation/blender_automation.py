import os
import subprocess

root = "/mnt/d/Blender Projects"
file_tree = ["Assets\Materials", "Renders", "References"]
blender_path = "/mnt/c/Program Files/Blender Foundation/Blender 2.83/blender.exe"

class Blender_Automation:
    def __init__(self, project_name):
        self.project_name = project_name
        self.file_tree = file_tree
        self.blender_path = blender_path
        self.root_path = root_path

    def createProject(self):
        self.projectName = os.path.join(self.rootPath, self.projectName)

        try:
            os.mkdir(self.projectName)

        except Exception:
            print("Project already exists.")
            sys.exit()
