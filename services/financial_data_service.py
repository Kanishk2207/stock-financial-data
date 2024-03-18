import csv
import datetime

from services.rc_db_service import RCDBService
from asyncmy.errors import DatabaseError
from fastapi import HTTPException
from sqlalchemy import insert, select

from models.db.financial_data import FinancialData

class FinancialDataService(RCDBService):
    def __init__(self, session):
        super().__init__(session)
        
    async def get_data_from_ticker(self, ticker, colomns = None, start_date = None):
        try:
            
            if colomns and start_date:
                
                attrubutes = [getattr(FinancialData, col) for col in colomns]
                statement = select(*attrubutes) \
                    .where(FinancialData.ticker == ticker) \
                    .where(FinancialData.date >= start_date)
                    
            elif colomns and not start_date:
                attrubutes = [getattr(FinancialData, col) for col in colomns]
                statement = select(*attrubutes) \
                    .where(FinancialData.ticker == ticker)
                    
            elif start_date and not colomns:
                
                statement = select(FinancialData) \
                    .where(FinancialData.ticker == ticker) \
                    .where(FinancialData.date >= start_date)
                    
            else:
                
                statement = select(FinancialData) \
                    .where(FinancialData.ticker == ticker)
            
            results = await self.session.execute(statement)
            
            lists = []
            
            for result in results:
                lists.append(result._asdict())
                
            return lists
        except DatabaseError as db_error:
            raise HTTPException(status_code=500, detail=f"Database Error: {str(db_error)}")
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"Internal Server Error1: {str(ex)}")

