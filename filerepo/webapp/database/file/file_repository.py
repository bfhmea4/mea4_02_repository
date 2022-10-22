from typing import Optional

from .file_dto import FileDTO
from ..file_system import FileSystem
from ...domain.file import FileRepository, File


class FileRepositoryImpl(FileRepository):
    """FileRepositoryImpl implements CRUD operations related File entity using SQLAlchemy."""

    def __init__(self, file_system: FileSystem):
        self.file_system: FileSystem = file_system

    def find_by_id(self, id: str) -> FileDTO:
        try:
            file_dto = self.file_system.read(id)
        except:
            raise

        return file_dto  # muss File zurückgegeben werden: .to_entity()

    def find_all(self) -> FileDTO:
        try:
            files_list = self.file_system.list_files()
        except:
            raise

        return files_list

    def create(self, file: File):
        file_dto = FileDTO.from_entity(file)
        try:
            self.file_system.write(file_dto)
        except:
            raise

    def delete_by_id(self, id: str):
        try:
            self.file_system.delete(id)
        except:
            raise

#    def update(self, book: Book):
#         book_dto = BookDTO.from_entity(book)
#         try:
#             _book = self.session.query(BookDTO).filter_by(id=book_dto.id).one()
#             _book.title = book_dto.title
#             _book.page = book_dto.page
#             _book.read_page = book_dto.read_page
#             _book.updated_at = book_dto.updated_at
#         except:
#             raise
#
#     def delete_by_id(self, id: str):
#         try:
#             self.session.query(BookDTO).filter_by(id=id).delete()
#         except:
#             raise
#
#
# class BookCommandUseCaseUnitOfWorkImpl(BookCommandUseCaseUnitOfWork):
#     def __init__(
#         self,
#         session: Session,
#         book_repository: BookRepository,
#     ):
#         self.session: Session = session
#         self.book_repository: BookRepository = book_repository
#
#     def begin(self):
#         self.session.begin()
#
#     def commit(self):
#         self.session.commit()
#
#     def rollback(self):
#         self.session.rollback()
