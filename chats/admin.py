from django.contrib import admin

from .models import Board, Message, User

admin.site.register(Board)
admin.site.register(Message)
admin.site.register(User)
