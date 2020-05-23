#!/usr/bin/python3
import os
import shutil
from extensions import file_extensions

class MyOrganiser:
    dest = "/mnt/d/FILE TESTING/TEST DEST"

    def search(self, curPath):
        """

        Walks the current directory and checks the file extensions 
        if it maches the values in the file_extensions dictionary
        
        param curPath: current working path

        """

        for files in os.listdir(curPath):
            fileName, fileExtension = os.path.splitext(files)         
            fileFormat = '{}{}'.format(fileName, fileExtension)

            self.moveFile(fileExtension, fileFormat)

    def makeSubDirs(self, dirs):
        """

        Makes a directory first that represents its main category 
        then makes subfolders that represents its sub categories

        param dirs: the new directories

        """
        
        try:
           os.makedirs(dirs)
        except Exception:
            pass

    def moveFile(self, fileExtension, file_format):
        """

        Once the current directory is walked, it will begin check if 
        the file extensions match the keys in the dictionary and if it does, 
        it will return the value of the key in the dictionary

        param fileExtension: the extension of the file
        param file_format: the name of the files + the file extension

        """

        for category in file_extensions.items():
            if fileExtension in category:
                self.subDirs = os.path.join(self.dest, category[1])
                self.filePrompt = file_format + '|' + str(category[1]) 

                self.makeSubDirs(self.subDirs)
               
                try:
                    shutil.move(file_format, self.subDirs)
                    print(self.filePrompt)
                   
                except Exception:
                    pass
        try:
            if not fileExtension in category:
                self.subDirs = os.path.join(self.dest, file_extensions['none'])

                self.makeSubDirs(self.subDirs)

                shutil.move(file_format, self.subDirs)
                print(file_format, str(category[1]), sep='|')

        except Exception:
            pass
        
if __name__ == "__main__":
    curPath = "/mnt/d/FILE TESTING/TEST ROOT"
    os.chdir(curPath)

    main = MyOrganiser()
    main.search(curPath)