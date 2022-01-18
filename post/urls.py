from django.urls import path 
from . import views 



app_name = 'post'

urlpatterns = [
    
    path('' , views.blog , name='blog'),
    path('search/' , views.search , name='search'),
    path('post/<int:pk>/' , views.post , name='post_detail'),
    
]
