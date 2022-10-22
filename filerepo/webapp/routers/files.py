from typing import List
from fastapi import File, UploadFile, status, APIRouter
from fastapi.responses import JSONResponse, FileResponse


from filerepo.webapp.schemas.file_schema import FileGetModel, FileUploadModel, FileDownloadModel
from filerepo.webapp.service.file_service import FileServiceImpl
from filerepo.webapp.database.file.file_repository import FileRepositoryImpl
from filerepo.webapp.database.file_system import FileSystem



router = APIRouter()
file_system = FileSystem()
file_repository = FileRepositoryImpl(file_system)
file_service = FileServiceImpl(file_repository)


@router.post("/files/upload", response_model=FileGetModel ,tags=["files"])
async def upload(file: UploadFile = File(...)):
    try:
        uploaded_file = {
                        "file_name":file.filename,
                        "file_type":file.content_type,
                        "file_content": file.file.read()
                         }
        return file_service.create(FileUploadModel(**uploaded_file))

    except FileNotFoundError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'message': str(e)}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"result": 'success'}
        )


@router.get("/files", response_model=List[FileGetModel], tags=["files"])
def files():
    return file_service.find_all()



#@router.delete("/files/{filename}", tags=["files"])
#def delete_file(filename: str):


#@router.get("/files/{filename}", tags=["files"])
#async def download_file(filename: str):



#@router.get("/files/{filename}/info", response_model=FileBase, tags=["files"])
#async def get_file_info(filename: str):
