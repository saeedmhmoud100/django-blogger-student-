from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.Login_user, name='login'),
    path('logout/', views.Logout_user, name='logout'),

]
