from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','email','password']


    def create(self, validated_data):
        User.objects.create_user(**validated_data)

        user ={
            "username": validated_data.get('username'),
            "password": validated_data.get('password'),
            "email": validated_data.get('email'),
        }

        return user


class CommentSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField()
    post=serializers.StringRelatedField()

    class Meta:
        model=Comments
        fields='__all__'
        read_only_fields=['owner','added_at','post']



class PostSerializer(serializers.ModelSerializer):

    comments=CommentSerializer(source="comment",read_only=True,many=True)

    class Meta:
        model=Post
        fields='__all__'
        read_only_fields=['owner','created_at']


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model=likes
        fields='__all__'
        read_only_fields=['owner','created_at','post']
        

