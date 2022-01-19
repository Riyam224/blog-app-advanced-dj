

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.urls import reverse



class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




class Comment(models.Model):
    post = models.ForeignKey('Post', verbose_name=_("post"), related_name='comments', on_delete=models.CASCADE)
    user =  models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)
    content = models.TextField(_("content"))


    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return str(self.user.username)



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
    content = models.TextField(_("content"))
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)
  

    author = models.ForeignKey(Author, verbose_name=_("author"), related_name='post_author', on_delete=models.CASCADE)
    thumbnail = models.ImageField(_("thumbnail"), upload_to='post/' , blank=True , null=True)
    category = models.ManyToManyField(Category, verbose_name=_("category"))
    featured = models.BooleanField(_("featured") , default=False)
    previous_post = models.ForeignKey("self", verbose_name=_("previous post"), related_name='previous', on_delete=models.SET_NULL , null=True , blank=True)
    next_post = models.ForeignKey("self", verbose_name=_("next post"),  related_name = 'next' ,on_delete=models.SET_NULL , null=True , blank=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post:post_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("post:post_update", kwargs={"pk": self.pk})
        
    def get_delete_url(self):
        return reverse("post:post_delete", kwargs={"pk": self.pk})

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
    
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    
    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()


     




