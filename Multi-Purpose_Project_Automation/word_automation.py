import subprocess
import os
from docx import Document

class Word_Automation:
    def __init__(self, project_name):
        self.project_name = project_name
        self.root_path = "/mnt/c/Users/lemue/Documents/School Projects"
        self.word_path = "/mnt/c/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
        self.document = Document()
                
    def word_automate(self):
        self.project_path = os.path.join(self.root_path, (self.project_name + '.docx'))
        self.document.save(self.project_path)
        subprocess.Popen(self.word_path, self.project_path)