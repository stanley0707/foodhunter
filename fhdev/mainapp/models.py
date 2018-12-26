from django.db import models
from django.conf import settings
from accounts.models import User


# Create your models here.
class ChatRoom(models.Model):
    """ chatroom model """
    creator = models.ForeignKey(User, verbose_name="создатель", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name='Участники', related_name="invited_user")
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    
    class Meta:
        verbose_name = "беседа"
        verbose_name_plural = "беседы"


class Chat(models.Model):
    """ chat model """
    room = models.ForeignKey(ChatRoom, verbose_name="Беседа", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField('сообщение', max_length=1000)
    date = models.DateTimeField('дата отправки', auto_now_add=True)

    class Meta:
        verbose_name = "cообщения"
        verbose_name_plural = "сообщения"

