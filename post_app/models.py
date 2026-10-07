from django.db import models
from django.contrib.auth.models import User





class Post(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="post_images")
    description=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):

    comment=models.TextField()
    added_at=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment")



