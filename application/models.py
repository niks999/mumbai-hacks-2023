from datetime import datetime
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Integer, Numeric, String, Text, func
from application.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    mobile_number = Column(String(20), unique=True, nullable=False)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Contractor(Base):
    __tablename__ = "contractor"

    id = Column(Integer, primary_key=True)
    mobile_number = Column(String(20), unique=True, nullable=False)
    name = Column(String(100))
    registration_number = Column(String(50), unique=True, nullable=False)
    rating = Column(Numeric(10,2), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Issue(Base):
    __tablename__ = "issue"

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    latitude = Column(Numeric(10,2), nullable=False)
    longitude = Column(Numeric(10,2), nullable=False)
    status = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    created_by_user_id = Column(Integer, nullable=False)
    contractor_id = Column(Integer)
    quotation_amount = Column(Numeric(10,2), nullable=True)
    quotation_duration = Column(Integer, nullable=True)
    raised_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    funding_expiry_at = Column(DateTime)
    work_deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True)
    issue_id = Column(Integer, nullable=False)
    image_url = Column(String(200), nullable=False)
    user_id = Column(Integer)
    contractor_id = Column(Integer)
    comment = Column(Text)
    uploaded_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Vote(Base):
    __tablename__ = "vote"

    id = Column(Integer, primary_key=True)
    issue_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    vote_type = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class IssueHistory(Base):
    __tablename__ = "issue_history"

    id = Column(Integer, primary_key=True)
    issue_id = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    changed_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Contribution(Base):
    __tablename__ = "contribution"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    issue_id = Column(Integer, nullable=False)
    contributed_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    is_refunded = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)