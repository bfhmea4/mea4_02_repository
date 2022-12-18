import unittest
from filerepo.webapp.repository.database import SessionLocal
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl
from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl
from filerepo.webapp.service.file_service import FileService, FileServiceImpl

session = SessionLocal()


class TestService(unittest.TestCase):
    service: FileService

    def setUp(self):
        session.begin()
        repository = FileRepositoryImpl(session)
        upload_repository = UploadActivityRepositoryImpl(session)
        TestService.service = FileServiceImpl(repository, upload_repository)

    def tearDown(self):
        session.close()

    def test_findAll(self):
        self.assertEqual(TestService.service.find_all(), [])

