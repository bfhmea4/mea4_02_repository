from typing import List

from filerepo.webapp.domain.file.file import File


class FileSystem():

    def __init__(self):
        self.directory = {}  # TypedDict[str, FileDTO] #funktioniert?

    def write(self, file: File):
        self.directory[file.id] = file

    def read(self, id: str) -> File:
        return self.directory.get(id)

    def delete(self, id: str):
        del self.directory[id]

    def list_files(self) -> List[File]:
        file_list: List[File] = []
        for file in self.directory.values():
            file_list.append(file)
        return file_list

