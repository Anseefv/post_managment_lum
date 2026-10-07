from django.urls import path
from .views import*
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('login/post',PostApiView,basename="post")

urlpatterns = [

    path('register/',RegisterApiView.as_view()),
    path('login/',ObtainAuthToken.as_view()),
    path('login/post/<int:id>/comment/',CommentApiView.as_view({

        'get': 'list',
        'post': 'create'
    }
    )),
    
    path('login/post/<int:id>/comment/<int:pk>/',CommentApiView.as_view({
            
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
        }
    ))
    
    

] + router.urls