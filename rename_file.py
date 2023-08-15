from PyPDF2 import PdfReader
import os
import string

_PATH = 'YOUR OWN PATH'
_EXTENSION = "pdf"

def _get_first_author(names: str) -> str:
    if ";" in names:
        names = names.partition(";")[0]
    elif "," in names:
        names = names.partition(",")[0] 
    names_splitted = [name.translate(str.maketrans('', '', string.punctuation)) for name in names.split(" ") if name]
    return names_splitted 

def _get_initials(names_splitted: list, length: int) -> list:
    initials_list = []
    for index in range(length):
        initials_list.extend(names_splitted[index][0])
    return initials_list

def _create_new_name(last_name: str, initials: list) -> str:
    if len(initials) == 0:
        return last_name
    else:
        return f"{last_name}, {'. '.join(initials)}."

def _get_author_name(names: str) -> str:
    if len(names) > 0:
        names_splitted = _get_first_author(names)
        length = len(names_splitted)-1
        initials_list = _get_initials(names_splitted, length)
        return _create_new_name(names_splitted[length], initials_list)

def _rename_file(dirpath: str, file_name: str):
    reader = PdfReader(open(f"{dirpath}/{file_name}", "rb")) 
    if reader.is_encrypted:
        reader.decrypt("")
    metadata = reader.metadata
    if metadata is not None:
        if metadata.author is not None and metadata.title is not None:
            author_name = _get_author_name(metadata.author)
            new_name = f"{author_name}_{metadata.title}"
            os.rename(f"{dirpath}/{file_name}", f"{dirpath}/{new_name}.{_EXTENSION}")

for (dirpath, dirnames, filenames) in os.walk(_PATH):
    for file in filenames:
        if file.rpartition(".")[2] == _EXTENSION:
            print("Current file:", file)
            _rename_file(dirpath, file)

print("Done.")