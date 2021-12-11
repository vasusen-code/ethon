#DroneBots/Vasusen-code/Maahi/shah/
#__ChauhanMahesh__

import pathlib

#get file extension using path of file
def file_extension(file_path):
    extension = pathlib.Path(f'{file_path}').suffix 
    return extension
