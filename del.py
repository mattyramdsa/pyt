import os
from pathlib import Path
import touch
myfile = "favtutor.txt"
Path(myfile).touch() #creating a new empty file
print("Files in a directory -->",os.listdir())
print("We can see a file created succesfully")
print("-----------------------------------------------------")
# If file exists, delete it.
if os.path.isfile(myfile):
    os.remove(myfile)
    print("Favtutor file deleted using remove() function")
    print("Current files in directory -->",os.listdir())
    print("-----------------------------------------------------")
else:
    # If it fails, inform the user.
    print("Error: %s file not found" % myfile)
