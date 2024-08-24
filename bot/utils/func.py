from asgiref.sync import sync_to_async

@sync_to_async
def guest_info(guest):
    return (
        f"*👤To'liq ismi:* {guest.full_name}\n" +
        (f"*🚻Jinsi:* {guest.get_sex_display()}\n" if guest.sex else "") +
        (f"*🌏Davlati:* {guest.state.name}\n" if guest.state else "") +
        (f"*🚨Guruhi*: {guest.name_of_group}\n" if guest.name_of_group else "") +
        (f"*⭕️Kategoriyasi:* {guest.categories.name}\n" if guest.categories else "") +
        (f"*💬Tillari:* {', '.join([lang.name for lang in guest.language.all()])}\n" if guest.language.all() else "") +
        (f"*👨‍💼Mas'ul odam:* {guest.liaison_person}\n" if guest.liaison_person else "") +
        (f"*🚘Samarqandagi transport:* {guest.transports_in_samarkand}\n" if guest.transports_in_samarkand else "") +
        (f"*🏠Samarqandagi mehmonhona:* {guest.hotel_in_samarkand}\n" if guest.hotel_in_samarkand else "") +
        (f"*💭Izoh:* {guest.comments}\n" if guest.comments else "") 
    )



@sync_to_async
def message_info(message):
    return str(
        
        f"*🔅Sarlavha:* {message.title}\n" +
        f"*💭Xabar:* {message.message}\n\n" +
        f"*⌛Jo'natilgan vaqti:* {message.created_at.strftime('%d/%m/%Y %H:%M')}"
    )
