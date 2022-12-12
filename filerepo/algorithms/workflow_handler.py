import asyncio
from filerepo.webapp.domain.workflow.workflow import Workflow
from filerepo.webapp.repository.file.file_dto import FileDTO

class WorkflowHandler():
    def __init__(self, workflow: Workflow,file: FileDTO):
        self.workflow = workflow
        self.file = file
    
    async def kickoff(self):
        if "inmage" in self.file.file_content:
            asyncio.sleep(3600)
            print("Slept well!!")
