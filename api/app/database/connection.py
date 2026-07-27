from sqlalchemy import create_engine

from common.config.settings import settings

'''
pool_pre_ping automatically checks if a pooled connection 
is still alive before using it, which helps avoid stale connection errors.
'''
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
)