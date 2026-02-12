from sqlalchemy import Column,Integer,String,Text,BigInteger

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    chat_id = Column(BigInteger,nullable=False,unique=True)
    phone = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    full_name = Column(Text)
    username = Column(String)