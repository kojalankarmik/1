from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    apartments = relationship('Apartment', back_populates='owner')
    leads = relationship('Lead', back_populates='user')

class Apartment(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    address = Column(String, nullable=False)
    media = relationship('Media', back_populates='apartment')
    posts = relationship('ChannelPost', back_populates='apartment')
    owner = relationship('User', back_populates='apartments')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    apartment_id = Column(Integer, ForeignKey('apartments.id'))
    url = Column(String, nullable=False)
    apartment = relationship('Apartment', back_populates='media')

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class ChannelPost(Base):
    __tablename__ = 'channel_posts'
    id = Column(Integer, primary_key=True)
    apartment_id = Column(Integer, ForeignKey('apartments.id'))
    content = Column(String, nullable=False)
    apartment = relationship('Apartment', back_populates='posts')

class Lead(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    apartment_id = Column(Integer, ForeignKey('apartments.id'))
    user = relationship('User', back_populates='leads')
    apartment = relationship('Apartment')

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    apartment_id = Column(Integer, ForeignKey('apartments.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    booking_date = Column(DateTime, default=datetime.utcnow)
    apartment = relationship('Apartment')
    user = relationship('User')

class ReferralCode(Base):
    __tablename__ = 'referral_codes'
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)

class ReferralEvent(Base):
    __tablename__ = 'referral_events'
    id = Column(Integer, primary_key=True)
    referral_code_id = Column(Integer, ForeignKey('referral_codes.id'))
    event_type = Column(Enum('signup', 'purchase', name='event_types'))

class Payout(Base):
    __tablename__ = 'payouts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)

class WebhookEvent(Base):
    __tablename__ = 'webhook_events'
    id = Column(Integer, primary_key=True)
    event_name = Column(String, nullable=False)

class HotOffer(Base):
    __tablename__ = 'hot_offers'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
