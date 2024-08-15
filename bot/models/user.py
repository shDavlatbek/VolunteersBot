from app.models import User, Guest, Message
from asgiref.sync import sync_to_async

@sync_to_async
def save_user_to_db(telegram_id, first_name, last_name) -> User:
    return User.objects.create(telegram_id=telegram_id, first_name=first_name, last_name=last_name)

@sync_to_async
def check_user_exists(telegram_id) -> bool:
    return True if User.objects.filter(telegram_id=telegram_id) else False

@sync_to_async
def get_user(telegram_id) -> User:
    return User.objects.filter(telegram_id=telegram_id).first()

@sync_to_async
def get_guests(user) -> list[Guest]:
    return list(user.guests.all())

@sync_to_async
def get_messages(user) -> list[Message]:
    return list(user.messages.all())

@sync_to_async
def get_guest_info(guest_id) -> Guest:
    return Guest.objects.filter(id=guest_id).first()

@sync_to_async
def get_message_info(message_id) -> Message:
    return Message.objects.filter(id=message_id).first()