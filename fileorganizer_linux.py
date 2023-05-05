import os
import sys
from datetime import datetime

import extensiondict


def cmd_args():
    src_base = sys.argv[1]  # The src_base is the folder path from which all files are copied out of
    dst_base = sys.argv[2]  # dst_base is the base destination folder path off of which all files are grouped off

    if not src_base.endswith('/'):
        src_base = src_base + '/'

    if not dst_base.endswith('/'):
        dst_base = dst_base + '/'

    return src_base, dst_base


def execute(src_base, dst_base):
    for filename in os.listdir(src_base):

        path = src_base + filename

        if os.path.isdir(path):
            folder_path = path + '/'
            execute(folder_path, dst_base)

        split = os.path.splitext(path)
        extension = split[1]

        try:
            dest = dst_base + extensiondict.extension_dict[extension.lower()]

            mdate = os.path.getctime(src_base + filename)
            year = datetime.fromtimestamp(int(mdate)).strftime("%Y")
            month = datetime.fromtimestamp(int(mdate)).strftime("%m")
            day = datetime.fromtimestamp(int(mdate)).strftime("%d")

            dest = f'{dest}/{year}/{month}/{day}'

            final_path_exists = os.path.exists(dest)

            if not final_path_exists:
                os.makedirs(dest)

            stripped_filename = filename.replace(" ", "\\ ").replace("'", "\\" + "\'")

            file_exists_in_dest = os.path.isfile(dest + '/' + filename)

            filepath = src_base + stripped_filename

            file_exists_in_src = os.path.isfile(src_base + filename)

            if file_exists_in_dest:
                print(filename + ' was not transferred from ' + src_base + ' to ', dest)
                not_moved = True

            else:
                if file_exists_in_src and not file_exists_in_dest:
                    movefile(filepath, dest)

        except:
            print(extension.lower() not in extensiondict.extension_dict.keys(),
                  f"Unknown extension: {extension.lower()}")


# movefile is the function that handles moving of files from source to destination folder
def movefile(src, dst):
    os.system('mv ' + src + ' ' + dst)


def run():
    """
    Orchestrator to run the functions
    """
    src_base, dst_base = cmd_args()
    execute(src_base, dst_base)


if __name__ == "__main__":
    run()
