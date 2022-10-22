from typing import TypedDict, List

from filerepo.webapp.database.file.file_dto import FileDTO


class FileSystem():

    def __init__(self):
        self.directory = {}  # TypedDict[str, FileDTO] #funktioniert?

    def write(self, file: FileDTO):
        self.directory[file.id] = file.to_entity()

    def read(self, id: str) -> FileDTO:
        return FileDTO.from_entity(self.directory.get(id))

    def delete(self, id: str):
        del self.directory[id]

    def list_files(self) -> List[FileDTO]:
        file_list: List[FileDTO] = []
        for file in self.directory.values():
            file_list.append(FileDTO.from_entity(file))
        return file_list

