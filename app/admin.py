from django.contrib import admin

from .models import User, Guest, Message
from .forms import MessageForm


class MessageAdmin(admin.ModelAdmin):
    form = MessageForm
    filter_horizontal = ('user',)

    class Media:
        js = ('app/custom_filter.js',)  

class UserAdmin(admin.ModelAdmin):
    search_fields = ['telegram_id', 'first_name', 'last_name']

    list_display = ['full_name', 'guests_list']
    list_filter = ['guests']
    
    
    def full_name(self, obj):
        return obj.full_name()
    
    
    def guests_list(self, obj):
        return obj.guests_list()
    
    
    full_name.admin_order_field = 'first_name'
    guests_list.admin_order_field = 'guests'


class GuestAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'name_of_group']
    list_filter = ['state', 'language', 'sex']
    list_display = ['full_name', 'name_of_group', 'state', 'sex']


admin.site.register(Message, MessageAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Guest, GuestAdmin)