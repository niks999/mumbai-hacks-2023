from decimal import Decimal

from application import db
from application.models import CreditHistory, Event, EventEnrolment, EventHistory, Moderator, User


class EventService:
    @staticmethod
    def create_event(
        title,
        description,
        area_name,
        category,
        created_by,
        reward_credits,
        event_timestamp,
        max_participants,
    ):
        event = Event(
            title=title,
            description=description,
            area_name=area_name,
            category=category,
            created_by=created_by,
            reward_credits=reward_credits,
            event_timestamp=event_timestamp,
            max_participants=max_participants,
            status=Event.STATUS_CREATED,
        )
        event.save()

        EventService.update_history(event)

        return event

    @staticmethod
    def get_event(event_id):
        return Event.query.get(event_id)

    @staticmethod
    def get_events():
        return Event.query.all()

    @staticmethod
    def update_event_status(event_id, status):
        event = Event.query.get(event_id)
        if not event:
            return None
        event.status = status
        event.save()

        EventService.update_history(event)

        return event

    @staticmethod
    def enroll_in_event(event_id, user_id):
        event = Event.query.get(event_id)
        if not event:
            return None

        user = User.query.get(user_id)
        if not user:
            return None

        enrolment = EventEnrolment.query.filter_by(event_id=event_id, user_id=user_id).first()
        if enrolment:
            return {"status": "SUCCESS", "message": "Already enrolled in event"}

        enrolment = EventEnrolment(event_id=event_id, user_id=user_id)
        enrolment.save()

        return {"status": "SUCCESS", "message": "Enrolled in event"}

    @staticmethod
    def remove_enrolment(event_id, user_id):
        enrolment = EventEnrolment.query.filter_by(event_id=event_id, user_id=user_id).first()
        if not enrolment:
            return {"status": "SUCCESS", "message": "Not enrolled in event"}

        db.session.delete(enrolment)
        db.session.commit()
        return {"status": "SUCCESS", "message": "Removed enrolment"}

    @staticmethod
    def update_history(event):
        history = EventHistory(event_id=event.id, status=event.status)
        history.save()


class UserService:
    @staticmethod
    def login(mobile_number):
        user = User.query.filter_by(mobile_number=mobile_number).first()
        if not user:
            user = User(mobile_number=mobile_number)
            user.save()

        # send OTP
        return user

    @staticmethod
    def get_details(user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return None
        return user

    @staticmethod
    def credit(user_id, event_id, amount):
        user = User.query.get(user_id)
        if not user:
            return None

        history = CreditHistory.query.filter_by(user_id=user_id, event_id=event_id).first()
        if history:
            return user

        CreditHistory(user_id=user_id, event_id=event_id, amount=amount).save()

        user.credits_earned = round(user.credits_earned + Decimal(amount), 2)
        user.credits_left = round(user.credits_left + Decimal(amount), 2)
        user.save()

        return user


class ModeratorService:
    @staticmethod
    def login(mobile_number):
        moderator = Moderator.query.filter_by(mobile_number=mobile_number).first()
        if not moderator:
            moderator = Moderator(mobile_number=mobile_number)
            moderator.save()

        # send OTP
        return moderator

    @staticmethod
    def get_details(moderator_id):
        moderator = Moderator.query.filter_by(id=moderator_id).first()
        if not moderator:
            return None
        return moderator
