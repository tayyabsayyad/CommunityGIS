from django.urls import path , include
from . import views

urlpatterns = [
	path('',views.front,name = 'front'),
    path('home/',views.home,name= 'home'),
    path('login/',views.login_user, name = 'login'),
    path('logout/',views.logout_user, name = 'logoutU'),


]
