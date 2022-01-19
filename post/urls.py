from django.urls import path 
from . import views 



app_name = 'post'

urlpatterns = [
    
    path('' , views.blog , name='blog'),
    path('search/' , views.search , name='search'),
    
    path('create/' , views.post_create , name='post_create'),
    path('<int:pk>/update/' , views.post_update , name='post_update'),
    path('<int:pk>/delete/' , views.post_delete , name='post_delete'),
   


    path('<int:pk>/' , views.post , name='post_detail'),
    
]
