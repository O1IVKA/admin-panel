from django.urls import path
from .views import ArticleCreate, ArticleDelete, ArticleUpdate

urlpatterns = [
    path('create', ArticleCreate.as_view(), name='create'),
    path('delete/<slug:slug>', ArticleDelete.as_view(), name='delete'),
    path('edit/<slug:slug>', ArticleUpdate.as_view(), name='edit'),
]
