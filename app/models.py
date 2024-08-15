from django.db import models
from django_countries.fields import CountryField

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
    guests = models.ManyToManyField(Guest, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Message(models.Model):
    user = models.ManyToManyField(User, related_name='messages')
    title = models.CharField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Language(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name