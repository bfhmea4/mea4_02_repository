import time

import asyncio
import numpy as np

from filerepo.webapp.domain.file.file import File
from filerepo.webapp.domain.workflow.workflow import Workflow


class WorkflowHandler():
    def __init__(self, workflow: Workflow, file: File):
        self.workflow = workflow
        self.file = file

    def kickoff(self):
        if "image" in self.file.file_type:
            asyncio.create_task(self.calculate_black_white_ratio())

    def calculate_black_white_ratio(self):
        time.sleep(10)
        nparr = np.frombuffer(self.file.file_content, np.uint8)
        print("Black: " + str(np.sum(nparr == 255)))
        print("White: " + str(np.sum(nparr == 0)))
        print("Black/White ratio: " + str(np.sum(nparr == 255) / np.sum(nparr == 0)))
