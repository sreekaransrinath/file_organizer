import os
from datetime import datetime
from time import strftime
import extensiondict


# The src_base_folder is the folder from which all files are copied out of
src_base = "/home/skaranzx16/Downloads/"  # Enter your source folder path here i.e., the folder you intend to clean up
# dst_base is the base destination folder off of which the filetype and year based file directory trees begin
dst_base = "/home/skaranzx16/"  # Enter your base destination folder path here

def cleandesk():
    for filename in os.listdir(src_base):
        i = 1

        split = os.path.splitext(src_base + filename)
        root_name = split[0]
        extension = split[1]
        print('The file ', root_name, ' is of the type ', extension)
        
        try:
            # Dest is the final argument for destination folder that I feed into the file copy method. It is updated with the appropriate filetype_and year-based directories using conditionals below
            dest = dst_base + extensiondict.extension_dict[extension.lower()]
            print('The destination folder based on file type is ', dest)

            mdate = os.path.getmtime(src_base + filename)
            year = datetime.fromtimestamp(int(mdate)).strftime("%Y") 
            print('The year of modification for this file is', year)

            dest = dest + "/" + year
            print("Destination folder with year added is", dest)

            year_exists = os.path.exists(dest)
            print("Does the appropriate year directory exist? ", year_exists)

            if not year_exists:
                os.makedirs(dest)
                year_exists = os.path.exists(dest)
                print("The year directory now exists.")
            
            print('The file name is ', filename)

            stripped_filename = filename.replace(" ", "\\ ")
            print('The stripped file name is ', stripped_filename)

            # file_exists_in_dest checks if the specified directory is a file, which indicates that the filename in fact exists. If it does, the block underneath this line either creates a new name by appending numbers to the end of the filename or leaves the file alone, based on a decision made by the user

            file_exists_in_dest = os.path.isfile(dest + '/' + filename)
            print('Does the file already exist in destination? ', file_exists_in_dest)

            filepath = src_base + stripped_filename
            print('The final source file path to be passed as argument is ', filepath)

            file_exists_in_src = os.path.isfile(filepath)

            if file_exists_in_dest:
                moveornot = input(filename + ' already exists in the destination directory. \nWould you like me to move the file to the destination after renaming it (or) leave it alone? \nPress 1 for the first option and press any other key to choose the second. ')

                if moveornot == '1':
                    while file_exists_in_dest:
                        i += 1
                        newpath = root_name + str(i) + extension
                        os.rename(filepath, newpath)
                        newpathsplit = newpath.split("/")
                        lastindex = len(newpathsplit)-1
                        newname = newpathsplit[lastindex]
                        movefile(newpath, dest)
                        file_exists_in_dest = os.path.isfile(dest + '/' + newname)
                        print('A name clash occurred in the process but was fixed.')
                        filename = newname
                
                else:
                    print('Alright, I\'ll leave it alone')
                    print(filename + ' was not transferred from ' + src_base + ' to ', dest)

            else:
                if file_exists_in_src and not file_exists_in_dest:
                    movefile(filepath, dest)

            if not os.path.isfile(src_base + filename):
                print(filename, ' was deleted from ', src_base, '\n\n')
            
            else:
                print(filename, ' was not deleted from ', src_base, '\n\n')

        except Exception:
            extension.lower() not in extensiondict.extension_dict.keys()


# movefile is the function that handles moving of files from source to destination folder
def movefile(src, dst):
    command = 'mv ' + src + ' ' + dst
    print('The command to be passed to shell is ', command)
    os.system(command)
    print("The file was successfully transferred")

# buildtree() is a function that checks whether you have the file organization system in place. If not, it creates the necessary trees for you
def buildtree():
    now = datetime.now()
    year = now.strftime('%Y')
    for path in extensiondict.extension_dict.values():
        command = dst_base + path + '/' + year + '/'
        try:
            if not os.path.exists(command):
                print('Does the path exist?', os.path.exists(command))
                print(command)
                os.makedirs(command)
        except FileExistsError:
            print("Directory already exists; not created")


buildtree()
cleandesk()
