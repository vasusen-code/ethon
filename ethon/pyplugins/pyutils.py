#DroneBots/Vasusen-code/Maahi/shah/
#__ChauhanMahesh__

import pathlib

#get file extension using path of file
def file_extension(file_path):
    extension = pathlib.Path(f'{file_path}').suffix 
    return extension

#make a list with limited length and check length
#Limit = maximun length of the list
def Q_length(List, limit):
    length = len(List)
    if length > int(limit) + 1:
        return 'FULL'
    else:
        return length
    
