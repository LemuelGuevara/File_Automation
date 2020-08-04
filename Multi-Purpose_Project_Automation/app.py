import os
import sys
from blender_automation import Blender_Automation
from Python_project_automation import Python_Project_Automation
from word_automation import Word_Automation

file_dict = {
    "py" : "Python",
    "word" : "Word",
    "blend" : "Blender"
}

class Main:
    def __init__(self, usr_input):
        self.usr_input = usr_input
        self.file_dict = file_dict

    def split_text(self):
        self.project_name, self.project_type = self.usr_input.split()
        self.project_type.lower()

    def find_type(self):
        if self.project_type == "py":
            python_auto = Python_Project_Automation(self.project_name)
            python_auto.createProject()
            python_auto.initProject()
            sys.exit()

        elif self.project_type == "word":
            word_auto = Word_Automation(self.project_name)
            word_auto.word_automate()
            sys.exit()

        elif self.project_type == "blend":
            blender_auto = Blender_Automation(self.project_name)
            blender_auto.createProject()
            sys.exit()

if __name__ == "__main__":

    print("Py = Python | Blend = Blender | Word = Word")

    usr_input = input("Create Project: ")

    app = Main(usr_input)
    app.split_text()
    app.find_type()
