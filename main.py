import shutil
import os
from datetime import datetime
from time import strftime

src_base = "/home/skaranzx16/Downloads/"
dst_base = "/home/skaranzx16/"

def cleandesk():
    for filename in os.listdir(src_base):
        i = 1
        split = os.path.splitext(src_base + filename)
        root_name = split[0]
        extension = split[1]
        print(extension)
        dest = dst_base + extension_dict[extension]
        print(dest)
        now = datetime.now()
        year = now.strftime("%Y")
        year_exists = False
        for foldername in os.listdir(dest):
            if foldername == year:
                dest = dest + "/" + year
                year_exists = True
        if year_exists == False:
            dest = dest + '/' + year
            os.mkdir(dest)
            year_exists = True
        file_exists = os.path.isfile(dest)
        while file_exists:
            i += 1
            newname = root_name + str(i) + extension
            newname = newname.split("/")[2]
            file_exists =  os.path.isfile(dest + '/' + newname)

        shutil.copy2(src_base + filename, dest)
        print(dest)
        print(filename + ' was transferred from ' + src_base + ' to ', dest)

        #filelist = [f for f in os.listdir(src_base)]
        #for f in filelist:
        #    os.remove(os.path.join(src_base, f))

extension_dict = {
#No name
    'noname' : "Other/Uncategorized",
#Audio
    '.aif' : "Media/Audio",
    '.cda' : "Media/Audio",
    '.mid' : "Media/Audio",
    '.midi' : "Media/Audio",
    '.mp3' : "Media/Audio",
    '.mpa' : "Media/Audio",
    '.ogg' : "Media/Audio",
    '.wav' : "Media/Audio",
    '.wma' : "Media/Audio",
    '.wpl' : "Media/Audio",
    '.m3u' : "Media/Audio",
#Text
    '.txt' : "Text/TextFiles",
    '.doc' : "Text/MicrosoftWord",
    '.docx' : "Text/MicrosoftWord",
    '.odt ' : "Text/TextFiles",
    '.pdf': "Text/PDF",
    '.rtf': "Text/TextFiles",
    '.tex': "Text/TextFiles",
    '.wks ': "Text/TextFiles",
    '.wps': "Text/TextFiles",
    '.wpd': "Text/TextFiles",
#Video
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
#Images
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
#Internet
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
#Compressed
    '.7z': "Other/Compressed",
    '.arj': "Other/Compressed",
    '.deb': "Other/Compressed",
    '.pkg': "Other/Compressed",
    '.rar': "Other/Compressed",
    '.rpm': "Other/Compressed",
    '.tar.gz': "Other/Compressed",
    '.z': "Other/Compressed",
    '.zip': "Other/Compressed",
#Disc
    '.bin': "Other/Disc",
    '.dmg': "Other/Disc",
    '.iso': "Other/Disc",
    '.toast': "Other/Disc",
    '.vcd': "Other/Disc",
#Data
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
#Executables
    '.apk': "Other/Executables",
    '.bat': "Other/Executables",
    '.com': "Other/Executables",
    '.exe': "Other/Executables",
    '.gadget': "Other/Executables",
    '.jar': "Other/Executables",
    '.wsf': "Other/Executables",
#Fonts
    '.fnt': "Other/Fonts",
    '.fon': "Other/Fonts",
    '.otf': "Other/Fonts",
    '.ttf': "Other/Fonts",
#Presentations
    '.key': "Text/Presentations",
    '.odp': "Text/Presentations",
    '.pps': "Text/Presentations",
    '.ppt': "Text/Presentations",
    '.pptx': "Text/Presentations",
#Programming
    '.c': "Programming/C&C++",
    '.class': "Programming/Java",
    '.dart': "Programming/Dart",
    '.py': "Programming/Python",
    '.sh': "Programming/Shell",
    '.swift': "Programming/Swift",
    '.html': "Programming/HTML",
    '.h': "Programming/C&C++",
#Spreadsheets
    '.ods' : "Text/Spreadsheets",
    '.xlr' : "Text/Spreadsheets",
    '.xls' : "Text/Spreadsheets",
    '.xlsx' : "Text/Spreadsheets",
#System
    '.bak' : "Text/Other/System",
    '.cab' : "Text/Other/System",
    '.cfg' : "Text/Other/System",
    '.cpl' : "Text/Other/System",
    '.cur' : "Text/Other/System",
    '.dll' : "Text/Other/System",
    '.dmp' : "Text/Other/System",
    '.drv' : "Text/Other/System",
    '.icns' : "Text/Other/System",
    '.ini' : "Text/Other/System",
    '.lnk' : "Text/Other/System",
    '.msi' : "Text/Other/System",
    '.sys' : "Text/Other/System",
    '.tmp' : "Text/Other/System"
}

cleandesk()
