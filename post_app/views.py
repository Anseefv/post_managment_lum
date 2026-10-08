from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from .permission import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

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

    permission_classes=[CommentPermission,IsAuthenticated]
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


class LikesApiView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[PostPermission,IsAuthenticated]

    def post(self,request,**kwargs):
        id=self.kwargs.get('id')
        post=Post.objects.get(id=id)
        ser=LikeSerializer(data=request.data)
        if likes.objects.filter(post=post,owner=request.user).exists():
            return Response({"message":"allready liked"})
        if ser.is_valid():
            ser.save(post=post,owner=request.user)
            return Response({"message":"like added"},status=status.HTTP_200_OK)
        return Response({"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,**kwargs):
        id=self.kwargs.get('id')
        post=Post.objects.get(id=id)
        if likes.objects.filter(post=post,owner=request.user).exists():
            likes.objects.get(post=post,owner=request.user).delete()
            return Response({"message":"unliked"},status=status.HTTP_200_OK)
        return Response({"message":"you are not liked"},status=status.HTTP_400_BAD_REQUEST)
            



