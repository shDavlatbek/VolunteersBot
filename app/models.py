from django.db import models
from django_countries.fields import CountryField

from bot.config_reader import config

TOKEN = config.bot_token.get_secret_value()

class Guest(models.Model):
    state = CountryField()
    full_name = models.CharField(max_length=300)
    name_of_group = models.CharField(max_length=200, blank=True, null=True)
    categories = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=[('M', 'Erkak'), ('F', 'Ayol')], blank=True, null=True)
    language = models.ManyToManyField('Language', blank=True)
    liaison_person = models.CharField(max_length=300, blank=True, null=True)
    
    
    comments = models.TextField(blank=True, null=True)
    hotel_in_tashkent = models.CharField(max_length=300, blank=True, null=True)
    transports_in_samarkand = models.CharField(max_length=300, blank=True, null=True)
    hotel_in_samarkand = models.CharField(max_length=300, blank=True, null=True)
    
    
    departure_from = models.CharField(max_length=300, blank=True, null=True)
    date_of_departure = models.DateTimeField(blank=True, null=True)
    departure_flight_number = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.full_name
    

class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    guests = models.ManyToManyField(Guest, blank=True, related_name='users')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Message(models.Model):
    user = models.ManyToManyField(User, related_name='messages', blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    title = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # Save the Message instance first to generate an ID
    #     all_users = User.objects.none()  # Initialize an empty queryset

    #     for category in self.category.all():
    #         # Filter Guests by category and then get the associated Users
    #         users_in_category = User.objects.filter(guests__in=Guest.objects.filter(categories=category))
    #         all_users = all_users | users_in_category  # Combine querysets of users

    #     # Remove duplicates (if any) by using distinct() 
    #     all_users = all_users.distinct()

    #     self.user.set(all_users)  # Add all users to the ManyToManyField
    #     super().save(*args, **kwargs)  # Save the Message instance again to update the user field

    
class Language(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name