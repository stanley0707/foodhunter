from django.contrib import admin
from .models  import ChatRoom, Chat
# Register your models here.

class ChatRoomAdmin(admin.ModelAdmin):
    """ to admin view """
    list_display = ("creator", "invited", "date")

    def invited(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])

class ChatAdmin(admin.ModelAdmin):
    """ dialogs """
    list_display = ('room', 'user', 'text', 'date')


admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Chat, ChatAdmin)
