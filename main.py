import os
from datetime import datetime
from time import strftime


def cleandesk():
    for filename in os.listdir(src_base):
        i = 1
        split = os.path.splitext(src_base + filename)
        root_name = split[0]
        extension = split[1]
        print('The file ', root_name, ' is of the type ', extension)
        try:
            # Dest is the final argument for destination folder that I feed into the file copy method. It is updated with the appropriate filetype_and year-based directories using conditionals below
            dest = dst_base + extension_dict[extension]
            print('The destination folder based on file type is ', dest)
            now = datetime.now()
            year = now.strftime("%Y")
            print('The year is', year)

            dest = dest + "/" + year
            print('The file name is ', filename)
            stripped_filename = filename.replace(" ", "\\ ")
            print('The stripped file name is ', stripped_filename)
            # file_exists checks if the specified directory is a file, which indicates that the filename in fact exists. If it does, the block underneath this line either creates a new name by appending numbers to the end of the filename or leaves the file alone, based on a decision made by the user
            file_exists = os.path.isfile(dest)
            print('File exists is ', file_exists)
            filepath = src_base + stripped_filename
            print('The final source file path to be passed as argument is ', filepath)
            if file_exists:
                dec = input(filename + ' already exists in the destination directory. \nWould you like me to move the file to the destination after renaming it (or) leave it alone? \nPress 1 for the first option and press any other key to choose the second. ')

                if dec == '1':
                    while file_exists:
                        i += 1
                        newname = root_name + str(i) + extension
                        newname = newname.split("/")[2]
                        file_exists = os.path.isfile(dest + '/' + newname)
                        os.rename(filepath, newname)
                        print('Trial number ', i, 'The modified source filepath is ', filepath)
                        movefile(filepath, dest)
                        print(dest)
                        print(filename + ' was transferred from ' + src_base + ' to ', dest, 'A name clash occurred in the process but was fixed.')
                else:
                    print('Alright, I\'ll leave it alone')
                    print(filename + ' was not transferred from ' + src_base + ' to ', dest)

            if file_exists == False and os.path.isfile(filepath):
                movefile(filepath, dest)
                print(filename + ' was transferred from ' + src_base + ' to ', dest)

            if not os.path.isfile(filepath):
                print(filename, ' was deleted from ', src_base, '\n\n')
            else:
                print(filename, ' was not deleted from ', src_base, '\n\n')

        except Exception:
            extension not in extension_dict.keys()


# movefile is the function that handles moving of files from source to destination folder
def movefile(src, dst):
    command = 'mv ' + src + ' ' + dst
    print(command)
    os.system(command)


# buildtree() is a function that checks whether you have the file organization system in place. If not, it creates the necessary trees for you
def buildtree():
    now = datetime.now()
    year = now.strftime('%Y')
    for path in extension_dict.values():
        command = dst_base + path + '/' + year + '/'
        try:
            if not os.path.exists(command):
                print('Does the path exist?', os.path.exists(command))
                print(command)
                os.makedirs(command)
        except Exception:
            os.path.exists(command)


extension_dict = {
    # No name
    'noname': "Other/Uncategorized",
    # Audio
    '.aif': "Media/Audio",
    '.cda': "Media/Audio",
    '.mid': "Media/Audio",
    '.midi': "Media/Audio",
    '.mp3': "Media/Audio",
    '.mpa': "Media/Audio",
    '.ogg': "Media/Audio",
    '.wav': "Media/Audio",
    '.wma': "Media/Audio",
    '.wpl': "Media/Audio",
    '.m3u': "Media/Audio",
    # Text
    '.txt': "Text/TextFiles",
    '.doc': "Text/Word",
    '.docx': "Text/Word",
    '.odt': "Text/Word",
    '.pdf': "Text/PDF",
    '.rtf': "Text/TextFiles",
    '.tex': "Text/TextFiles",
    '.wks': "Text/TextFiles",
    '.wps': "Text/TextFiles",
    '.wpd': "Text/TextFiles",
    # Video
    '.3g2': "Media/Video",
    '.3gp': "Media/Video",
    '.avi': "Media/Video",
    '.flv': "Media/Video",
    '.h264': "Media/Video",
    '.m4v': "Media/Video",
    '.mkv': "Media/Video",
    '.mov': "Media/Video",
    '.mp4': "Media/Video",
    '.mpg': "Media/Video",
    '.mpeg': "Media/Video",
    '.rm': "Media/Video",
    '.swf': "Media/Video",
    '.vob': "Media/Video",
    '.wmv': "Media/Video",
    # Images
    '.ai': "Media/Images",
    '.bmp': "Media/Images",
    '.gif': "Media/Images",
    '.ico': "Media/Images",
    '.jpg': "Media/Images",
    '.jpeg': "Media/Images",
    '.png': "Media/Images",
    '.ps': "Media/Images",
    '.psd': "Media/Images",
    '.svg': "Media/Images",
    '.tif': "Media/Images",
    '.tiff': "Media/Images",
    '.CR2': "Media/Images",
    # Internet
    '.asp': "Other/Internet",
    '.aspx': "Other/Internet",
    '.cer': "Other/Internet",
    '.cfm': "Other/Internet",
    '.cgi': "Other/Internet",
    '.pl': "Other/Internet",
    '.css': "Other/Internet",
    '.htm': "Other/Internet",
    '.js': "Other/Internet",
    '.jsp': "Other/Internet",
    '.part': "Other/Internet",
    '.php': "Other/Internet",
    '.rss': "Other/Internet",
    '.xhtml': "Other/Internet",
    # Compressed
    '.7z': "Other/Compressed",
    '.arj': "Other/Compressed",
    '.deb': "Other/Compressed",
    '.pkg': "Other/Compressed",
    '.rar': "Other/Compressed",
    '.rpm': "Other/Compressed",
    '.gz': "Other/Compressed",
    '.xz': "Other/Compressed",
    '.z': "Other/Compressed",
    '.zip': "Other/Compressed",
    '.tgz': "Other/Compressed",
    # Disc
    '.bin': "Other/Disc",
    '.dmg': "Other/Disc",
    '.iso': "Other/Disc",
    '.toast': "Other/Disc",
    '.vcd': "Other/Disc",
    # Data
    '.csv': "Programming/Database",
    '.dat': "Programming/Database",
    '.db': "Programming/Database",
    '.dbf': "Programming/Database",
    '.log': "Programming/Database",
    '.mdb': "Programming/Database",
    '.sav': "Programming/Database",
    '.sql': "Programming/Database",
    '.tar': "Programming/Database",
    '.xml': "Programming/Database",
    '.json': "Programming/Database",
    # Executables
    '.apk': "Other/Executables",
    '.bat': "Other/Executables",
    '.com': "Other/Executables",
    '.exe': "Other/Executables",
    '.gadget': "Other/Executables",
    '.jar': "Other/Executables",
    '.wsf': "Other/Executables",
    # Fonts
    '.fnt': "Other/Fonts",
    '.fon': "Other/Fonts",
    '.otf': "Other/Fonts",
    '.ttf': "Other/Fonts",
    # Presentations
    '.key': "Text/Presentations",
    '.odp': "Text/Presentations",
    '.pps': "Text/Presentations",
    '.ppt': "Text/Presentations",
    '.pptx': "Text/Presentations",
    # Programming
    '.c': "Programming/C++andC",
    '.class': "Programming/Java",
    '.dart': "Programming/Dart",
    '.py': "Programming/Python",
    '.sh': "Programming/Shell",
    '.swift': "Programming/Swift",
    '.html': "Programming/HTML",
    '.h': "Programming/C++andC",
    # Spreadsheets
    '.ods': "Text/Spreadsheets",
    '.xlr': "Text/Spreadsheets",
    '.xls': "Text/Spreadsheets",
    '.xlsx': "Text/Spreadsheets",
    # System
    '.bak': "Text/Other/System",
    '.cab': "Text/Other/System",
    '.cfg': "Text/Other/System",
    '.cpl': "Text/Other/System",
    '.cur': "Text/Other/System",
    '.dll': "Text/Other/System",
    '.dmp': "Text/Other/System",
    '.drv': "Text/Other/System",
    '.icns': "Text/Other/System",
    '.ini': "Text/Other/System",
    '.lnk': "Text/Other/System",
    '.msi': "Text/Other/System",
    '.sys': "Text/Other/System",
    '.tmp': "Text/Other/System"
}

# The src_base_folder is the folder from which all files are copied out of
src_base = "/home/skaranzx16/Downloads/"  # Enter your source folder path here i.e., the folder you intend to clean up
# dst_base is the base destination folder off of which the filetype and year based file directory trees begin
dst_base = "/home/skaranzx16/"  # Enter your base destination folder path here

buildtree()
cleandesk()
