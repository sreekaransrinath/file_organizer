# file_organizer

A script that looks through any folder you tell it to and moves the files to respective subfolders based on the file type.

The organizational system for this were borrowed from github.com/kallehallden, but I feel like my implementation is different enough for this to deserve it's own repo.

Tried using the shutil module to do shutil.copy2() at first, but realized that that was erasing parts of metadata that I wanted to preserve for files, so I've switched to using the os module to move files.

AFAIK all issues that existed have been resolved with the latest commit, but I can still think of a ton of features that I could still implement in this.

Will keep updating as I work on this.
