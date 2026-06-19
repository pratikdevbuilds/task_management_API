from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

from src.utils.setting import settings
Base=declarative_base()


engine = create_engine(url=settings.db_url)

LocalSession= sessionmaker(bind= engine)

# for getting session object 
def get_db():
    session=LocalSession()
    try:
        yield session
    finally:
        session.close()
 