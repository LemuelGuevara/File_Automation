#!/usr/bin/python3
import os
import sys
import shutil
from extensions import file_extensions

class MyOrganiser:
    dest = "D:\ARCHIVED FILES"

    def search(self, curPath):
        """
        Walks the current directory and checks the file extensions if it maches
        the values in the file_extensions dictionary
        param: current working path
        """

        for files in os.listdir(curPath):
            file_name, file_extension = os.path.splitext(files)         
            new_file_name = '{}{}'.format(file_name, file_extension)

            self.moveFile(file_extension, new_file_name)

    def moveFile(self, extension, file_format):
        """
        Once the current directory is walked, it will begin check if the file 
        extensions match the keys in the dictionary and if it does, it will return
        the value of the key in the dictionary
        param: file_extension, file_name_format
        """
        
        for category in file_extensions.items():
            if extension in category:
                self.newPath = os.path.join(self.dest, category[1])

                shutil.move(file_format, self.newPath)
                print(file_format, str(category[1]), sep='|')
            
            # if not extension in category:
            #     self.miscFiles = os.path.join(self.dest, file_extensions['none'])

            #     print("File is not categorized and placed in the Misc Files")
            #     shutil.move(file_format, self.miscFiles)


if __name__ == "__main__":
    curPath = os.getcwd()
    os.chdir(curPath)

    main = MyOrganiser()
    main.search(curPath)


