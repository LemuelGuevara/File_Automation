import os
import sys
from blender_automation import Blender_Automation

file_dict = {
    "py" : "Python"
    "word" : "Word",
    "blend" : "Blender"
}

class Main:
    def __init__(self, project_name):
        self.project_name = project_name
        self.file_dict = file_dict

    def show_prompts(self):
        prompts = ["py = Python",
                   "word = Word Document",
                   "blend = Blender_Project"]

        print(prompts)

    def split_text(self):


    def automate(self):
        if self.project_name.endswith("py"):



if __name__ == "__main__":
    usr_input = input("Create Project: ")

    app = Main(usr_input)
    app.automate()
