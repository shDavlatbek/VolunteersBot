import time
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Message

from config.config_reader import config
import requests

TOKEN = config.bot_token.get_secret_value()

def message_info(message):
    return str(
        f"*Sarlavha:* {message.title}\n" +
        f"*Xabar:* {message.message}\n\n" +
        f"*Jo'natilgan vaqti:* {message.created_at.strftime('%d/%m/%Y %H:%M')}"
    )

def send_message(chat_id, message):
    bot_token = TOKEN

    response = requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage", 
        data={
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }
    )
    print(response)
    

@receiver(post_save, sender=Message.user.through)
def notify_bot(sender, instance, *args, **kwargs):
    user_ids = instance.user.all().values_list('telegram_id', flat=True)
    if user_ids:
        message = f"*Sizga yangi xabar keldi!*\n{message_info(instance)}"
        for user_id in user_ids:
            send_message(chat_id=user_id, message=message)
