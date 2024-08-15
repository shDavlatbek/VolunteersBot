from django.contrib import admin

from .models import User, Guest, Language, Message

admin.site.register([User, Guest, Message, Language])