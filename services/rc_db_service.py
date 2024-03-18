from os import environ as env
from sqlalchemy.ext.asyncio import AsyncSession

class RCDBService(object):

    def __init__(self, session: AsyncSession):
        self.session = session
        self.env = env
