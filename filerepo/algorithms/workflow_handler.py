import threading

import time
import numpy as np

from filerepo.webapp.domain.file.file import File
from filerepo.webapp.domain.workflow.workflow import Workflow

from filerepo.webapp.domain.workflow.workflow_repository import WorkflowRepository


class WorkflowHandler():
    def __init__(self,workflow: Workflow, workflowRepo: WorkflowRepository, file: File):
        self.workflow: Workflow = workflow
        self.workflowRepo: WorkflowRepository = workflowRepo
        self.file = file

    def kickoff(self):
        if "image" in self.file.file_type:
            t1 = threading.Thread(target=self.calculate_black_white_ratio)
            return t1.start()

    def calculate_black_white_ratio(self):
        time.sleep(10)
        nparr = np.frombuffer(self.file.file_content, np.uint8)
        print("Black: " + str(np.sum(nparr == 255)))
        print("White: " + str(np.sum(nparr == 0)))
        print("Black/White ratio: " + str(np.sum(nparr == 255) / np.sum(nparr == 0)))
        self.workflowRepo.update_status(True,self.workflow.id)
