from typing import Iterator

import unittest

from fastapi import Depends

from filerepo.webapp.repository.database import SessionLocal
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl
from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl
from filerepo.webapp.service.file_service import FileService, FileServiceImpl
from sqlalchemy.orm.session import Session


class TestService(unittest.TestCase):
    session: Session
    service: FileService

    @classmethod
    def setUpClass(cls):
        TestService.session = SessionLocal()
        repository = FileRepositoryImpl(TestService.session)
        upload_repository = UploadActivityRepositoryImpl(TestService.session)
        TestService.service = FileServiceImpl(repository, upload_repository)

    @classmethod
    def tearDownClass(cls):
        TestService.session.close()

    def test_finsAll(self):
        self.assertEqual(TestService.service.find_all(), [])
