from django.contrib import admin

from .models import User, Guest, Language, Message
from .forms import MessageForm

# class MessageAdmin(admin.ModelAdmin):
#     form = MessageForm
#     list_display = ['title', 'created_at']
#     search_fields = ['title', 'message']

class MessageAdmin(admin.ModelAdmin):
    # Include your model fields here
    filter_horizontal = ('user', 'categories')  # To use a horizontal filter widget for M2M fields

    class Media:
        js = ('app/custom_filter.js',)  # Link to the custom JavaScript file

admin.site.register(Message, MessageAdmin)
admin.site.register([User, Guest, Language])