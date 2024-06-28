from django.contrib import admin
from .models import Message, Chat

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'text', 'created_at', 'author', 'receiver')
    list_display = ('chat', 'author', 'receiver', 'created_at', 'text')
    # search_fields = ('author', 'text',)

# Register your models here.

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
