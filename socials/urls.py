from django.urls import path
from . import views 


urlpatterns = [
    path('',views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('create/', views.create_post, name='create'),
    path('addprofile/',views.addprofile, name='addprofile'),
    path('userprofile/',views.profile, name='userprofile'),
    path('photo/<str:pk>/', views.viewPhoto,name='photo'),
    path('like/<int:pk>', views.LikeView, name='likeview'),
    path('comment/<str:pk>/',views.Comment, name='comment'),
   
]
