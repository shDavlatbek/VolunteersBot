from app.models import User, Guest, Message
from asgiref.sync import sync_to_async

@sync_to_async
def crete_or_update_user(**kwargs) -> User:
    return User.objects.update_or_create(**kwargs)

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