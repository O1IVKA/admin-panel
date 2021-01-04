from django.urls import path
from .views import LogIn, LogOut, Reg

urlpatterns = [
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('registration/', Reg.as_view(), name='reg'),

]
