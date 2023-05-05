import argparse
import os
from datetime import datetime

import extensiondict


def execute(source: str, output: str, delete_sub_folder: bool = False):
    for filename in os.listdir(source):

        path = source + filename

        if os.path.isdir(path):
            folder_path = path + '/'
            execute(folder_path, output)
            if delete_sub_folder:
                delete_folder(folder_path)

        else:
            split = os.path.splitext(path)
            extension = split[1]

            try:
                dest = output + extensiondict.extension_dict[extension.lower()]

                file_date = os.path.getctime(source + filename)
                year = datetime.fromtimestamp(int(file_date)).strftime("%Y")
                month = datetime.fromtimestamp(int(file_date)).strftime("%m")
                day = datetime.fromtimestamp(int(file_date)).strftime("%d")

                dest = f'{dest}/{year}/{month}/{day}'

                final_path_exists = os.path.exists(dest)

                if not final_path_exists:
                    os.makedirs(dest)

                stripped_filename = filename.replace(" ", "\\ ").replace("'", "\\" + "\'")

                file_exists_in_dest = os.path.isfile(dest + '/' + filename)

                filepath = source + stripped_filename

                file_exists_in_src = os.path.isfile(source + filename)

                if file_exists_in_dest:
                    print(filename + ' was not transferred from ' + source + ' to ', dest)

                else:
                    if file_exists_in_src and not file_exists_in_dest:
                        movefile(filepath, dest)

            except:
                print(f"Unknown extension: {extension.lower()}")


# movefile is the function that handles moving of files from source to destination folder
def movefile(src, dst):
    os.system('mv ' + src + ' ' + dst)


# movefile is the function that handles moving of files from source to destination folder
def delete_folder(src):
    os.system('rm -r ' + src)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='File Organizer',
        description='Looks through any folder and subfolder you tell it to and moves the files to respective '
                    'sub folders based on the file type and dates.')

    parser.add_argument('-s', '--source', type=str,
                        help='Source folder where to look for files')

    parser.add_argument('-o', '--output', type=str,
                        help='Output folder where to save organized files')

    parser.add_argument('-d', '--delete', action='store_true',
                        help='Delete processed sub folders')

    args = parser.parse_args()

    src_base = args.source
    dst_base = args.output

    if not src_base.endswith('/'):
        src_base = src_base + '/'

    if not dst_base.endswith('/'):
        dst_base = dst_base + '/'

    execute(src_base, dst_base, args.delete)
