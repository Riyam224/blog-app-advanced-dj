
from atexit import register
from distutils import command
from django.contrib import admin

# Register your models here.
from .models import Author , Category , Post , Comment , PostView

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)