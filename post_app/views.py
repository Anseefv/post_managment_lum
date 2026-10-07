from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from .permission import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class RegisterApiView(CreateAPIView):

    serializer_class=RegistrationSerializer


class PostApiView(ModelViewSet):

    permission_classes=[PostPermission,IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=PostSerializer
    queryset=Post.objects.all()


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class CommentApiView(ModelViewSet):

    permission_classes=[PostPermission,IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=CommentSerializer

    def get_queryset(self):
        id=self.kwargs.get('id')
        post=Post.objects.get(id=id)
        return Comments.objects.filter(post=post)

    def perform_create(self, serializer):
        id=self.kwargs.get('id')
        post=Post.objects.get(id=id)
        return serializer.save(owner=self.request.user,post=post)

