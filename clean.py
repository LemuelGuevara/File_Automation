#!/usr/bin/python3
import os
import shutil
from extensions import file_extensions

class MyOrganiser:
    dest = "D:\ARCHIVED FIlES"

    def search(self, curPath):
        for files in os.listdir(curPath):
            file_name, file_extension = os.path.splitext(files)         
            new_file_name = '{}{}'.format(file_name, file_extension)

            self.moveFile(file_extension, new_file_name)

    def moveFile(self, extension, file_format):
        for key in file_extensions.items():
            if extension in key:
                self.newPath = os.path.join(self.dest, key[1])
                shutil.move(file_format, self.newPath)

                print(file_format, str(key[1]), sep='|')

if __name__ == "__main__":
    curPath = os.getcwd()
    os.chdir(curPath)

    main = MyOrganiser()
    main.search(curPath)


