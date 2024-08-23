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

class UserAdmin(admin.ModelAdmin):
    # Specify the fields you want to be searchable
    search_fields = ['telegram_id', 'first_name', 'last_name']

    # Optionally, you can also customize the list display and other options
    list_display = ['telegram_id', 'first_name', 'last_name']
    list_filter = ['guests']


class GuestAdmin(admin.ModelAdmin):
    # Specify which fields should be searchable
    search_fields = ['full_name', 'name_of_group']
    
    # Specify which fields should be used for filtering in the admin interface
    list_filter = ['state', 'language', 'sex']
    
    # Optionally, you can customize the list display
    list_display = ['full_name', 'name_of_group', 'state', 'sex']

admin.site.register(Message, MessageAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Guest, GuestAdmin)