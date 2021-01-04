from django.contrib import admin

from .models import Article, Picture, Tag
from users.models import Userc

admin.site.register(Userc)


@admin.register(Article)

@admin.register(Picture)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

