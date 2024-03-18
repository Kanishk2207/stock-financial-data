from fastapi import APIRouter, UploadFile, Depends, HTTPException, File

from sqlalchemy.ext.asyncio import AsyncSession

from services import data_injestion_service
from internal.databases.mysql import get_db


router = APIRouter()

@router.post('/upload', tags=['data-injestin'])
async def upload(file: UploadFile = File(...), mysql_session: AsyncSession = Depends(get_db) ):
    try:
        data_injestion_srv = data_injestion_service.DataInjestionService(mysql_session)
        
        data = await data_injestion_srv.read_and_upload_csv_file(file.filename)
        
        return {
            "message": data
        }
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(ex)}")