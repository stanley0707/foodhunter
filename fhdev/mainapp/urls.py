from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('chat/', ChatRoomView.as_view()),
    path('dialog/', DialogView.as_view()),
    path('created/', AddUserView.as_view()),
    path('users/', AddFriensToChat.as_view()),
    path('account/', include("accounts.urls"))   
]