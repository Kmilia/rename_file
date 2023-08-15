from PyPDF2 import PdfReader
import os

_PATH = 'papers/'
_EXTENSION = "pdf"

def _get_author_name(names: str):
    names = names.partition(",")[0]
    names_splitted = names.split(" ")
    length = len(names_splitted)-1
    initials_list = []
    for index in range(length):
        initials_list.extend(names_splitted[index][0])
    if len(initials_list) == 0:
        return names_splitted[length]
    else:
        return f"{names_splitted[length]}, {'. '.join(initials_list)}."

def _rename_file(dirpath: str, file_name: str):
    reader = PdfReader(open(f"{dirpath}/{file_name}", "rb")) 
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