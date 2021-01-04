from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from users.models import Userc



class Article(models.Model):
    """model for posts"""
    author = models.ForeignKey(Userc, related_name='author', on_delete=models.CASCADE, verbose_name='Автор',
                               default=None, blank=True, null=True)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    date = models.DateTimeField(auto_now=True)
    upd = models.BooleanField(default=False, blank=True)
    lenta = models.BooleanField(default=False, blank=True)
    simple = models.BooleanField(default=True, blank=True)
    slug = models.SlugField(default=None, max_length=160, unique=True)
    likes = models.ManyToManyField(Userc, default=None, blank=True)
    img = models.ImageField(upload_to='pm', null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('poster', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('edit', kwargs={'slug': self.slug})

    def get_absolute_url_del(self):
        return reverse('delete', kwargs={'slug': self.slug})


class Picture(models.Model):
    """model for pictures"""
    post = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='pm', blank=True, null=True)

    def __str__(self):
        return self.post.title
