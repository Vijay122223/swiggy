from django.urls import path
from .views import home,menu,signin,signup

urlpatterns = [
    path('home/',home ,name='home'),
    path('menu/',menu ,name='menu'),
    path('signin/',signin ,name='signin'),
    path('signup',signup,name='signup')
   

]
