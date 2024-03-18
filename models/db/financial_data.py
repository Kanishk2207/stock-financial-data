from models.db.RCBase import RCDBBase
import datetime

from sqlalchemy.orm import Mapped, MappedColumn
from sqlalchemy import String, Date, Integer, BigInteger

class FinancialData(RCDBBase):
    __tablename__ = 'financial_data'
    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    ticker: Mapped[str] = MappedColumn(String(50))
    date: Mapped[datetime.date] =  MappedColumn(Date)
    revenue: Mapped[int] = MappedColumn(BigInteger)
    gp: Mapped[int] = MappedColumn(BigInteger)
    fcf: Mapped[int] = MappedColumn(BigInteger)
    capex: Mapped[int] = MappedColumn(BigInteger)



# Table: financial_data

# Columns:
# 	id	int AI PK
# 	ticker	varchar(50)
# 	date	date
# 	revenue	int
# 	gp	int
# 	fcf	int
# 	capex	int
