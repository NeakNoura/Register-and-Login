from django.urls import path
from .views import home,register_view
from . import views
urlpatterns = [
    path('',home,name='home'),
    path('register/',register_view,name="register"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout")
]
