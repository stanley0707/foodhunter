import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from accounts.models import User, EmailActivation, CkookAccount, DefaultUserAccount
from .models import ChatRoom, Chat

from .serializers import (
    UserSerializers,
    ChatRoomSerializers,
    ChatSerializers,
    ChatPostSerializers,
    #EmailActivateSerializers,
    UserRegistrSerializers,
    AccountSerializers
)


class ChatRoomView(APIView):
    """ APIView to ChatRoom model """
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        room = ChatRoom.objects.all()
        serializer = ChatRoomSerializers(room, many=True)
        return Response({'data': serializer.data})

class DialogView(APIView):
    """ View for chat GET/POST """

    #permission_classes = [permissions.AllowAny, ]
    # authorization api
    # Now, for authentifications user must get POST url 
    # auth/... with username and password
    permission_classes = (IsAuthenticated,) 
    #authentication_classes = (TokenAuthentication)   
    
    def get(self, request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({'data': serializer.data})
    
    def post(self, request):
        #room  = request.data.get('room')
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)

class AddUserView(APIView):
    """ Add new user """
    
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serialized = UserRegistrSerializers(data=request.data)
        
        if serialized.is_valid() and request.data.get('ckook') == 'true':
            serialized.save()
            CkookAccount.objects.create()
            return Response(status=201)
        
        elif serialized.is_valid() and request.data.get('ckook') == 'false':
            serialized.save()
            DefaultUserAccount.objects.create()
            return Response(status=201)
        
        else:
            return Response(status=400)

#class AccountView(APIView):
#    permission_classes = (IsAuthenticated, )
#
#    def  get(self, request):
#        account = AccountSerializers(data=request.data)
#        user

class AddFriensToChat(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get('room')
        user = request.data.get('user')
        try:    
            room = Chat.objects.get(room=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)
