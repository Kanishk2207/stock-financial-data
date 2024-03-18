import csv

from services.rc_db_service import RCDBService
from datetime import datetime
from asyncmy.errors import DatabaseError
from fastapi import HTTPException
from sqlalchemy import insert

from models.db.financial_data import FinancialData



class DataInjestionService(RCDBService):
    def __init__(self, session):
        super().__init__(session)
    
    async def read_and_upload_csv_file(self, file):
        try:
            with open('external/csv_docs/Sample-Data-Historic.csv', 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                count = 0
                financial_data_list = []
                
                for row in reader:
                    # Parse the date string into datetime object
                    date_str = row['date']
                    
                    try:
                        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                        formatted_date = date_obj.strftime('%Y-%m-%d')  # Convert to 'YYYY-MM-DD' format
                        
                    except ValueError:
                        # Handle invalid date format
                        count += 1
                        print(f"Invalid date format for row: {row}", count)
                        continue
                    

                    ticker = row.get('ticker')
                    revenue = row.get('revenue')
                    gp = row.get('gp')
                    fcf = row.get('fcf')
                    capex = row.get('capex')


                    # Create a dictionary with formatted date
                    financial_data = {
                        'ticker': ticker if ticker else None,
                        'date': formatted_date,
                        'revenue': revenue if revenue else None,
                        'gp': gp if gp else None,
                        'fcf': fcf if fcf else None,
                        'capex': capex if capex else None
                    }
                    
                    # Append the dictionary to the list
                    financial_data_list.append(financial_data)
                    
                await self.session.execute(
                    insert(FinancialData),financial_data_list
                )
                    
                
                await self.session.commit()
                # print(list)
                return financial_data_list
                            
        except DatabaseError as db_error:
            await self.session.rollback()
            raise HTTPException(status_code=500, detail=f"Database Error: {str(db_error)}")
        except Exception as ex:
            await self.session.rollback()
            raise HTTPException(status_code=500, detail=f"Internal Server Error1: {str(ex)}")