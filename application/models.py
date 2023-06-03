from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, Text

from application.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    mobile_number = Column(String(255), unique=True, nullable=False)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    aadhaar_number = Column(String(255), unique=True)
    profile_image = Column(Text)
    is_moderator = Column(Boolean, default=False)
    credits_earned = Column(Numeric(10, 2), default=0)
    credits_left = Column(Numeric(10, 2), default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __init__(self, mobile_number):
        self.mobile_number = mobile_number

    def to_dict(self):
        return {
            "id": self.id,
            "mobile_number": self.mobile_number,
            "name": self.name,
            "email": self.email,
            "aadhaar_number": self.aadhaar_number,
            "profile_image": self.profile_image,
            "is_moderator": self.is_moderator,
            "credits_earned": self.credits_earned,
            "credits_left": self.credits_left,
            "created_at": self.created_at,
        }


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text, nullable=False)
    area_name = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    created_by = Column(String(255), nullable=False)
    reward_credits = Column(Numeric(10, 2), nullable=False)
    moderator_id = Column(Integer)
    event_timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    max_participants = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __init__(
        self,
        description,
        area_name,
        status,
        category,
        created_by,
        reward_credits,
        event_timestamp,
        max_participants,
    ):
        self.description = description
        self.area_name = area_name
        self.status = status
        self.category = category
        self.created_by = created_by
        self.reward_credits = reward_credits
        self.event_timestamp = event_timestamp
        self.max_participants = max_participants

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "area_name": self.area_name,
            "status": self.status,
            "category": self.category,
            "created_by": self.created_by,
            "reward_credits": self.reward_credits,
            "moderator_id": self.moderator_id,
            "event_timestamp": self.event_timestamp,
            "max_participants": self.max_participants,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class EventEnrolment(Base):
    __tablename__ = "event_enrolment"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    enrolled_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __init__(self, event_id, user_id):
        self.event_id = event_id
        self.user_id = user_id


class EventHistory(Base):
    __tablename__ = "event_history"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    status = Column(String(255), nullable=False)
    changed_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __init__(self, issue_id, status):
        self.issue_id = issue_id
        self.status = status


class CreditHistory(Base):
    __tablename__ = "credit_history"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    credited_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __init__(self, user_id, event_id, amount):
        self.user_id = user_id
        self.event_id = event_id
        self.amount = amount
