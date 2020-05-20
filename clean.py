#!/usr/bin/python3
import os
import sys
import shutil
from extensions import file_extensions

class MyOrganiser:
    dest = "/mnt/d/FILE TESTING/TEST DEST"

    def search(self, curPath):
        """

        Walks the current directory and checks the file extensions 
        if it maches the values in the file_extensions dictionary
        
        param: current working path

        """

        for files in os.listdir(curPath):
            file_name, file_extension = os.path.splitext(files)         
            new_file_name = '{}{}'.format(file_name, file_extension)

            self.moveFile(file_extension, new_file_name)

    def makeSubDirs(self, dirs):
        """

        Makes a directory first that represents its main category 
        then makes subfolders that represents its sub categories

        """
        
        try:
           os.makedirs(dirs)
        except Exception:
            pass

    def moveFile(self, f_extension, file_format):
        """

        Once the current directory is walked, it will begin check if 
        the file extensions match the keys in the dictionary and if it does, 
        it will return the value of the key in the dictionary

        param: file_extension, file_name_format

        """
    
        for category in file_extensions.items():
            if f_extension in category:
                self.subDirs = os.path.join(self.dest, category[1])
                self.filePrompt = file_format + '|' + str(category[1]) 
                
                self.makeSubDirs(self.subDirs)

                try:
                    shutil.move(file_format, self.subDirs)
                    print(self.filePrompt)

                except Exception:
                    pass

            """In proccess"""
            # try:
            #     if not extension in category:
            #         self.subDirs = os.path.join(self.dest, file_extensions['none'])

            #         shutil.move(file_format, self.subDirs)
            #         print(file_format, str(category[1]), sep='|')
            # except Exception:
            #     pass

if __name__ == "__main__":
    curPath = "/mnt/d/FILE TESTING/TEST ROOT"
    os.chdir(curPath)

    main = MyOrganiser()
    main.search(curPath)



