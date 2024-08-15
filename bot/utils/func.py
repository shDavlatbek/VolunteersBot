from asgiref.sync import sync_to_async

@sync_to_async
def guest_info(guest):
    return (
        f"*To'liq ismi:* {guest.full_name}\n" +
        (f"*Jinsi:* {guest.get_sex_display()}\n" if guest.sex else "") +
        (f"*Davlati:* {guest.state.name}\n" if guest.state else "") +
        (f"*Tug'ilgan sanasi:* {guest.date_of_birth.strftime('%d/%m/%Y')}\n" if guest.date_of_birth else "") +
        (f"*Guruhi*: {guest.name_of_group}\n" if guest.name_of_group else "") +
        (f"*Kategoriyasi:* {guest.categories.name}\n" if guest.categories else "") +
        (f"*Tillari:* {', '.join([lang.name for lang in guest.language.all()])}\n" if guest.language.all() else "") +
        (f"*Telefon raqami:* {guest.phone_number}\n" if guest.phone_number else "") +
        (f"*Email:* {guest.email}\n" if guest.email else "")
    )



@sync_to_async
def message_info(message):
    return str(
        (f"*Kategoriya:* {message.category}\n" if message.category else "") +
        f"*Sarlavha:* {message.title}\n" +
        f"*Xabar:* {message.message}\n\n" +
        f"*Jo'natilgan vaqti:* {message.created_at.strftime('%d/%m/%Y %H:%M')}"
    )
