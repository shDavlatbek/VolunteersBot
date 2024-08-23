from django.db import models
from django_countries.fields import CountryField

import requests

from bot.config_reader import config

TOKEN = config.bot_token.get_secret_value()

class Guest(models.Model):
    state = CountryField()
    full_name = models.CharField(max_length=300)
    name_of_group = models.CharField(max_length=200, blank=True, null=True)
    categories = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    passport_number = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    passport_issue_date = models.DateField(blank=True, null=True)
    passport_expiry_date = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=10, choices=[('M', 'Erkak'), ('F', 'Ayol')], blank=True, null=True)
    visa = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    language = models.ManyToManyField('Language', blank=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    
    
    liaison_person = models.CharField(max_length=300, blank=True, null=True)
    flight_path = models.CharField(max_length=300, blank=True, null=True)
    date_of_arrival = models.DateTimeField(blank=True, null=True)
    flight_number = models.CharField(max_length=200, blank=True, null=True)
    
    
    comments = models.TextField(blank=True, null=True)
    hotel_in_tashkent = models.CharField(max_length=300, blank=True, null=True)
    transports_in_tashkent = models.CharField(max_length=300, blank=True, null=True)
    tashken_samarkand = models.CharField(max_length=300, blank=True, null=True)
    transports_in_samarkand = models.CharField(max_length=300, blank=True, null=True)
    hotel_in_samarkand = models.CharField(max_length=300, blank=True, null=True)
    
    
    departure_from = models.CharField(max_length=300, blank=True, null=True)
    date_of_departure = models.DateTimeField(blank=True, null=True)
    departure_flight_number = models.CharField(max_length=200, blank=True, null=True)
    departed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.full_name
    

class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    guests = models.ManyToManyField(Guest, blank=True, related_name='users')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Message(models.Model):
    user = models.ManyToManyField(User, related_name='messages', blank=True)
    title = models.CharField(max_length=300)
    category = models.ManyToManyField('Category', blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    
    def __message_info(self):
        categories = self.category.all()
        return str(
            (f"*Kategoriya:* {', '.join([str(category) for category in categories])}\n" if categories.exists() else "") +
            f"*Sarlavha:* {self.title}\n" +
            f"*Xabar:* {self.message}\n\n" +
            f"*Jo'natilgan vaqti:* {self.created_at.strftime('%d/%m/%Y %H:%M')}"
        )
        

    def __send_message(self, chat_id, message):
        bot_token = TOKEN

        response = requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage", 
            data={
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'Markdown'
            }
        )
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the Message instance first to generate an ID
        all_users = User.objects.none()  # Initialize an empty queryset

        for category in self.category.all():
            # Filter Guests by category and then get the associated Users
            users_in_category = User.objects.filter(guests__in=Guest.objects.filter(categories=category))
            all_users = all_users | users_in_category  # Combine querysets of users

        # Remove duplicates (if any) by using distinct() 
        all_users = all_users.distinct()

        self.user.set(all_users)  # Add all users to the ManyToManyField
        super().save(*args, **kwargs)  # Save the Message instance again to update the user field
        
        # user_ids = self.user.all().values_list('telegram_id', flat=True)
        # print("user.all()", self.user.all().__dict__)
        # print("user_ids", user_ids)
        # message = f"*Sizga yangi xabar keldi!*\n{self.__message_info()}"
        # for user_id in user_ids:
        #     self.__send_message(chat_id=user_id, message=message)

    
class Language(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name