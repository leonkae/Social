from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout')
]
