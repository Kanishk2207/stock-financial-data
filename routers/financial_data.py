import datetime

from fastapi import APIRouter, UploadFile, Depends, HTTPException, File, Query
from sqlalchemy.ext.asyncio import AsyncSession

from services import financial_data_service
from internal.databases.mysql import get_db


router = APIRouter()

@router.get('/Api/', tags=['finantial-data'])
async def get_data(
    ticker: str = Query(..., alias="ticker"),
    column: str = Query(None, alias="column"),
    period: str = Query(None, alias="period"),
    mysql_session: AsyncSession = Depends(get_db)
    ):
    try:
        financial_data_srv = financial_data_service.FinancialDataService(mysql_session)
        
        columns = None
        start_date = None
        if column:
            columns = column.split(',')

        
        if period:
            years = int(period[:-1])
            today = datetime.date.today()
            start_date = today - datetime.timedelta(days=365 * years)
        
        data = await financial_data_srv.get_data_from_ticker(ticker, columns, start_date)
        
        
        return {
            "message": data
        }
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(ex)}")