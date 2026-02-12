from sqlalchemy import URL,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

from utils import settings


url_object = URL.create(
    'postgresql+psycopg2',
    settings.DB_USER,
    settings.DB_PASS,
    settings.DB_HOST,
    settings.DB_PORT,
    settings.DB_NAME
)

engine = create_engine(url_object)
Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False, bind=engine)