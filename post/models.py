from email import charset
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Author(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    profile_img = models.ImageField(_("profile image "), upload_to='author/' , blank=True , null=True)

    

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.user.username




class Category(models.Model):
    """Model definition for Category."""
    title = models.CharField(max_length=200)

  

    class Meta:
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.title





class Post(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField(_("overview"))
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)
    comment_count = models.IntegerField(_("comment count") , default=0)
    author = models.ForeignKey(Author, verbose_name=_("author"), related_name='post_author', on_delete=models.CASCADE)
    thumbnail = models.ImageField(_("thumbnail"), upload_to='post/' , blank=True , null=True)
    category = models.ManyToManyField(Category, verbose_name=_("category"))
    featured = models.BooleanField(_("featured") , default=False)

    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title
