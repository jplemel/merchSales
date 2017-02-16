from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import events
from base import Base

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key = True)
    
    #Foreign key
    merchID = Column(Integer, ForeignKey(merch.id))
    numSold = Column(Integer)
    #Foreign key
    eventID = Column(Integer, ForeignKey(event.id))


def __repr__(self):

    return 'Sale ID: {} Merch ID Sold: {} Number of Items Sold: {}'.format(self.id, self.merchID, self.numSold)
