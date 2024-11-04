from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name="home"),
    path('registration/',views.sign_up,name="sign_up"),
    path('login/',views.signin, name="login"),
    path('logout/',views.logout, name='logout'),
]