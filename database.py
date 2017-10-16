# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker

db = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Offers(Base):
    __tablename__ = 'offers'

    id = Column(Integer, primary_key=True)
    olx_id = Column(Integer, unique=True)
    name = Column(String)
    price = Column(Integer)
    location = Column(String)
    date = Column(String)
    link = Column(String)
    archive = Column(Boolean)

    def __repr__(self):
        return "<Offer(id={}, name={}, price={}, location={}, date={}, link={}, archive={})>".format(self.id,
                                                                                                     self.name,
                                                                                                     self.price,
                                                                                                     self.location,
                                                                                                     self.date,
                                                                                                     self.link,
                                                                                                     self.archive
                                                                                                     )

def update_offers_table(json_object):
    for offer in json_object:
        db_offer = session.query(Offers).filter_by(olx_id=offer['olx_id']).first()
        if not db_offer:
            new_offer = Offers(name=offer['name'],
                               price=offer['price'],
                               location=offer['location'],
                               date=offer['date'],
                               link=offer['link'],
                               olx_id=offer['olx_id'],
                               archive=False
                               )
            session.add(new_offer)
        else:
            db_offer.price = offer['price']
            db_offer.link = offer['link']
            session.add(db_offer)
    session.commit()

def get_offers(max_price):
    offers = session.query(Offers).filter_by(archive=False).filter(Offers.price <= max_price).order_by(Offers.id.asc()).all()
    return offers

def create_database():
    Base.metadata.create_all(db)