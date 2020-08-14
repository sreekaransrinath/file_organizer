# file_organizer

This script is designed to sort the contents of a target folder/directory into sub-folders-sub-directories based on the file type.

# Prerequisites
This script was written using stock Python packages. All packages used for this script are already part of the Python Standard Library. No additional dependencies.

# Command Line Arguments

The preferred way to run this script is using command line as a Superuser/Administrator on your Device. Only two arguments need to be passed:
* The source folder/directory.
* The base destination folder/directory.

# Deployment
To run the script via the command line, use the following code:

### On Windows:
Once command prompt is open as administrator, change directory to the folder containing fileorginizer using the "cd" command. For Example:
```
cd "C:\Users\[username]\Downloads\file_organizer
```
Once the directory is changed, use the following command:
```
python fileorganizer_windows.py [source_folder] [base_destination_folder] 
```         
Replace the [source_folder] [base_destination_folder] with appropriate path for the respective folders.

### On Linux:
Open the terminal in root mode by using "sudo" command. Then change directory to the sub-directory containing file_orginizer using the "cd" command. For example
```
cd ~/Downloads/file_organizer
```
Once in the directory, use the following command to deploy file_organizer:
```            
python3 fileorganizer_linux.py [source_folder] [base_destination_folder]
```
Replace the [source_folder] [base_destination_folder] placeholders with appropriate path for the respective directories.

Happy Organizing!


