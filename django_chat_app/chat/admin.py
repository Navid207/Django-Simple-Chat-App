from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    fields = ('text', 'created_at', 'author', 'receiver')
    list_display = ('author', 'receiver', 'created_at', 'text')
    # search_fields = ('author', 'text',)

# Register your models here.

admin.site.register(Message, MessageAdmin)

