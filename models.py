from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, BigInteger
import decimal

Base = declarative_base()

class Jsonable(Base):
    __abstract__ = True

    def to_dict(self):
        return {
            c.name: (
                getattr(self, c.name).__str__() if isinstance(getattr(self, c.name), datetime)
                else str(getattr(self, c.name)) if isinstance(getattr(self, c.name), decimal.Decimal)
                else getattr(self, c.name)
            )
            for c in self.__table__.columns 
        }
    
class Account(Jsonable):
    __tablename__ = "accounts"
    nickname = Column(String, primary_key=True)
    likes = Column(BigInteger, default=0)
    comments = Column(BigInteger, default=0)
    caption = Column(String, default="")
    updated_at = 
    