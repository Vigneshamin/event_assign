from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('delete_booking/<str:id>/', views.deleteBooking, name="delete_booking"),
    path('update_event/<str:id>/', views.updateEvent, name="update_event"),
    path('delete_event/<str:id>/', views.deleteEvent, name="delete_event"),
    path('create_event/', views.createevent, name="create_event"),
    path('view_profile/<str:id>/', views.viewprofile, name="view_profile"),

]