from datetime import datetime

from flask import Blueprint, request

from application.db import init_schema
from application.services import EventService, ModeratorService, UserService

bp = Blueprint("routes", __name__)


@bp.route("/init-db", methods=["POST"])
def init_db():
    init_schema()
    return {"status": "SUCCESS", "message": "Database initialized"}


@bp.route("/events", methods=["POST"])
def create_event():
    event = EventService.create_event(
        title=request.json["title"],
        description=request.json["description"],
        area_name=request.json["area_name"],
        category=request.json["category"],
        created_by=request.json["created_by"],
        reward_credits=request.json["reward_credits"],
        event_timestamp=datetime.strptime(request.json["event_timestamp"], "%Y-%m-%d %H:%M:%S"),
        max_participants=request.json["max_participants"],
    )
    return event.to_dict()


@bp.route("/events", methods=["GET"])
def get_events():
    events = EventService.get_events()
    return {"events": [event.to_dict() for event in events]}


@bp.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = EventService.get_event(event_id)
    return event.to_dict()


@bp.route("/events/<int:event_id>/status", methods=["PUT"])
def update_event_status(event_id):
    event = EventService.update_event_status(event_id, request.json["status"])
    return event.to_dict()


@bp.route("/events/<int:event_id>/enrolment", methods=["POST"])
def enroll_in_event(event_id):
    return EventService.enroll_in_event(event_id, request.json["user_id"])


@bp.route("/events/<int:event_id>/enrolment", methods=["DELETE"])
def remove_enrolment(event_id):
    return EventService.remove_enrolment(event_id, request.json["user_id"])


@bp.route("/users/login", methods=["POST"])
def user_login():
    user = UserService.login(request.json["mobile_number"])
    return {"status": "SUCCESS", "message": "OTP sent to mobile number"}


@bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserService.get_details(user_id)
    return user.to_dict()


@bp.route("/users/<int:user_id>/credit", methods=["POST"])
def credit_user(user_id):
    event_id = request.json["event_id"]
    amount = request.json["amount"]
    user = UserService.credit(user_id, event_id, amount)
    return user.to_dict()


@bp.route("/moderators/login", methods=["POST"])
def moderator_login():
    moderator = ModeratorService.login(request.json["mobile_number"])
    return {"status": "SUCCESS", "message": "OTP sent to mobile number"}


@bp.route("/verify-otp", methods=["POST"])
def verify_otp():
    user_id = request.json.get("user_id")
    moderator_id = request.json.get("moderator_id")
    if moderator_id:
        moderator = ModeratorService.get_details(moderator_id)
        if not moderator:
            return {}
        return moderator.to_dict()
    elif user_id:
        user = UserService.get_details(user_id)
        if not user:
            return {}
        return user.to_dict()


@bp.route("/leaderboard", methods=["GET"])
def leaderboard():
    return {"leaderboard": UserService.leaderboard()}
