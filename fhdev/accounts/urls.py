from django.conf.urls import url
from django.urls import path

from .views import (
        AccountEmailActivateView,
    )
#from mainapp.views import AccountView

urlpatterns = [
    url(r'email/confirm/(?P<key>[0-9A-Za-z]+)/$', 
            AccountEmailActivateView.as_view(), 
            name='email-activate'),
    
    path('email/resend-activation/', 
            AccountEmailActivateView.as_view(), 
            name='resend-activation'),
    
    #path('home/', AccountView.as_view()),
    
]